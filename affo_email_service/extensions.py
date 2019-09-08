import os

from celery import Celery

from flask_mail import Mail

from flask_marshmallow import Marshmallow

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy


__all__ = ["db", "ma", "mail", "migrate", "celery"]

db = SQLAlchemy(session_options={"autocommit": True})

ma = Marshmallow()

mail = Mail()

migrate = Migrate(directory=os.path.join(os.path.dirname(os.path.abspath(__file__)), "migrations"))

celery = Celery()
