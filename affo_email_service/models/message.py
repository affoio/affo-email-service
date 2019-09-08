import datetime

from sqlalchemy_utils import ScalarListType

from affo_email_service import const
from affo_email_service.extensions import db, ma


class Message(db.Model):  # noqa
    id = db.Column(db.Integer(), primary_key=True)
    from_ = db.Column(db.String(256))
    to = db.Column(ScalarListType())
    cc = db.Column(ScalarListType(), nullable=True)
    bcc = db.Column(ScalarListType(), nullable=True)
    subject = db.Column(db.String(256))
    text = db.Column(db.Text(), nullable=True)
    html = db.Column(db.Text(), nullable=True)
    attachment = db.Column(db.Boolean(), default=False)
    tag = db.Column(db.String(64))
    status = db.Column(
        db.Enum(
            const.MESSAGE_STATUS_NEW,
            const.MESSAGE_STATUS_PENDING,
            const.MESSAGE_STATUS_FAILED,
            const.MESSAGE_STATUS_SUCCEDED,
            const.MESSAGE_STATUS_SKIPPED,
            const.MESSAGE_STATUS_PARTIALLY_SKIPPED,
        )
    )
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class MessageSchema(ma.ModelSchema):
    class Meta:
        model = Message
        exclude = ("attachment",)


message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)
