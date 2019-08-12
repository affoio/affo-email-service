import sqlalchemy

from affo_email_service import const
from affo_email_service.extensions import db
from affo_email_service.models.message import Message, message_schema
from affo_email_service.models.unsubscribe import Unsubscribe
from affo_email_service.tasks.email import send_email


def send_from_dict(message):
    message_status = const.MESSAGE_STATUS_NEW

    with db.session.begin(subtransactions=True):
        # Ensure unsubscribes
        unsubscribes = db.session.query(Unsubscribe).filter(
            sqlalchemy.and_(Unsubscribe.email.in_(message['to']),
                            Unsubscribe.tag == message['tag'])
        )

        unsubscribes = set((u.email for u in unsubscribes))

        if unsubscribes:
            message_status = const.MESSAGE_STATUS_SKIPPED

        message_to = list(set(message['to']) - unsubscribes)

        if message_to:
            message_status = const.MESSAGE_STATUS_PARTIALLY_SKIPPED

            # Hold subscribed addresses only
            message['to'] = message_to

        # Create a message
        message_ = Message(
            from_=message['from_'],
            to=message['to'],
            cc=message.get('cc', None),
            bcc=message.get('bcc', None),
            subject=message['subject'],
            text=message['text'],
            html=message['html'],
            attachment=bool(message.get('attachments', None)),
            tag=message['tag'],
            status=message_status
        )
        db.session.add(message_)

    # Send the message
    if message_status in (const.MESSAGE_STATUS_NEW, const.MESSAGE_STATUS_PARTIALLY_SKIPPED):
        send_email.delay(message_id=message_.id)

    return message_schema.jsonify(message_)
