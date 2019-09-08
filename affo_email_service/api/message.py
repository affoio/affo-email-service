from affo_email_service.models.message import message_schema
from affo_email_service.services import email_service


def create(message):
    # FIXME: attachments aren't supported

    return message_schema.jsonify(email_service.send(**message)), 201
