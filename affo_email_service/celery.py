from affo_email_service.application import create_app, create_celery

app = create_app()
celery = create_celery(app)
