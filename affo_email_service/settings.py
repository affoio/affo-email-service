import sys  # noqa

from dynaconf import LazySettings, Validator

settings = LazySettings(ENVVAR_PREFIX_FOR_DYNACONF="AFFO_ES", ENVVAR_FOR_DYNACONF="AFFO_ES_SETTINGS")

# Register validators
settings.validators.register(
    Validator("DATABASE_URI", "CELERY_BROKER_URL", "EMAIL_HOST", "EMAIL_PORT", must_exist=True),
    Validator("EMAIL_PORT", is_type_of=int),
)

# Fire the validator
settings.validators.validate()

# SECRET CONFIGURATION
SECRET_KEY = getattr(settings, "SECRET_KEY", "")

# DEBUG CONFIGURATION
DEBUG = getattr(settings, "DEBUG", False)

# SQLALCHEMY CONFIGURATION
SQLALCHEMY_DATABASE_URI = settings.DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MODEL_IMPORTS = ("affo_email_service.models.message", "affo_email_service.models.unsubscribe")

# CELERY CONFIGURATION
CELERY_BROKER_URL = settings.CELERY_BROKER_URL
CELERY_IMPORTS = ("affo_email_service.tasks.email",)

# MAIL CONFIGURATION
MAIL_SERVER = settings.EMAIL_HOST
MAIL_USERNAME = getattr(settings, "EMAIL_HOST_USER", None)
MAIL_PASSWORD = getattr(settings, "EMAIL_HOST_PASSWORD", None)
MAIL_PORT = settings.EMAIL_PORT
MAIL_USE_TLS = getattr(settings, "EMAIL_USE_TLS", False)
MAIL_SUPPRESS_SEND = getattr(settings, "EMAIL_SUPPRESS_SEND", False)

settings.populate_obj(sys.modules[__name__])
