import sqlalchemy

from affo_email_service import const
from affo_email_service.extensions import db
from affo_email_service.models.message import Message
from affo_email_service.models.unsubscribe import Unsubscribe
from affo_email_service.tasks.email import send_email


class EmailService:
    def send(
        self, from_, to, subject, text, html, tag, attachments=None, cc=None, bcc=None
    ):
        message_status = const.MESSAGE_STATUS_NEW

        with db.session.begin(subtransactions=True):
            # Ensure unsubscribes
            unsubscribes = db.session.query(Unsubscribe).filter(
                sqlalchemy.and_(Unsubscribe.email.in_(to), Unsubscribe.tag == tag)
            )

            unsubscribes = set((u.email for u in unsubscribes))

            if unsubscribes:
                message_status = const.MESSAGE_STATUS_SKIPPED

            message_to = list(set(to) - unsubscribes)

            if message_to:
                message_status = const.MESSAGE_STATUS_PARTIALLY_SKIPPED

                # Hold subscribed addresses only
                to = message_to

            # Create a message
            message_ = Message(
                from_=from_,
                to=to,
                cc=cc,
                bcc=bcc,
                subject=subject,
                text=text,
                html=html,
                attachment=bool(attachments),
                tag=tag,
                status=message_status,
            )
            db.session.add(message_)

        # Send the message
        if message_status in (
            const.MESSAGE_STATUS_NEW,
            const.MESSAGE_STATUS_PARTIALLY_SKIPPED,
        ):
            send_email.delay(message_id=message_.id)

        return message_
