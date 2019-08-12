from .feedback import feedback_bp
from .template import template_bp
from .unsubscribe import unsubscribe_bp


def init_app(app):
    app.register_blueprint(feedback_bp)
    app.register_blueprint(template_bp)
    app.register_blueprint(unsubscribe_bp)
