import smtplib

import flask_mail

from sqlalchemy.orm.exc import NoResultFound

from affo_email_service.extensions import celery, db, mail  # noqa
from affo_email_service.models.message import Message


@celery.task(autoretry_for=(smtplib.SMTPException, NoResultFound), retry_backoff=True)
def send_email(message_id):
    message = db.session.query(Message).filter(Message.id == message_id).one()

    email = flask_mail.Message(
        recipients=message.to,
        sender=message.from_,
        body=message.text,
        subject=message.subject,
        cc=message.cc,
        bcc=message.bcc,
        html=message.html,
    )

    # FIXME: attachments aren't supported
    mail.send(email)
