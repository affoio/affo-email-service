import importlib
import logging

import connexion

import connexion_buzz

import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.flask import FlaskIntegration

from . import routes, settings, VERSION
from .extensions import celery, db, ma, mail, migrate

__all__ = ["create_celery", "create_app"]

logging.basicConfig(level=logging.INFO)


def create_celery(app, settings_override=None):
    if settings_override:
        app.config.update(settings_override)

    celery.config_from_object(app.config, namespace="CELERY")

    TaskBase = celery.Task

    class ContextTask(TaskBase):  # noqa
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


def create_app(settings_override=None):
    app = connexion.App(__name__, specification_dir="./spec/", options={"swagger_ui": False}, debug=settings.DEBUG)
    app.add_api("openapi.yaml", arguments={"title": "AFFO Email Service API"})
    app.app.register_error_handler(connexion_buzz.ConnexionBuzz, connexion_buzz.ConnexionBuzz.build_error_handler())

    application = app.app
    application.config.from_object(settings)

    if settings_override:
        application.config.update(settings_override)

    # Import DB models. Flask-SQLAlchemy doesn't do this automatically.
    with application.app_context():
        for module in application.config.get("SQLALCHEMY_MODEL_IMPORTS", list()):
            importlib.import_module(module)

    # Initialize extensions/add-ons/plugins.
    db.init_app(application)
    ma.init_app(application)
    mail.init_app(application)
    migrate.init_app(application, db)
    routes.init_app(application)

    sentry_sdk.init(
        integrations=[CeleryIntegration(), FlaskIntegration()],
        dsn=application.config.get("SENTRY_DSN"),
        environment=application.config.get("ENV"),
        release=VERSION,
    )

    return application
