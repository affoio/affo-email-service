import datetime

from affo_email_service.extensions import db


class Unsubscribe(db.Model):  # noqa
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(256))
    tag = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
