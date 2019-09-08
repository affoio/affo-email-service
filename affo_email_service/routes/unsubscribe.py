import flask

import itsdangerous

from affo_email_service import settings
from affo_email_service.extensions import db
from affo_email_service.models.unsubscribe import Unsubscribe


unsubscribe_bp = flask.Blueprint("unsubscribe", __name__, url_prefix="/unsubscribe")


@unsubscribe_bp.route("/<token>/")
def unsubscribe(token):
    safe = itsdangerous.URLSafeTimedSerializer(settings.SECRET_KEY)

    token_data = safe.loads(token)

    with db.session.begin(subtransactions=True):
        # Create an unsubscribe
        unsubscribe_ = Unsubscribe(**token_data)
        db.session.add(unsubscribe_)

    return flask.render_template("unsubscribe.html"), 200
