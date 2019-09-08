import json

import flask

import requests

feedback_bp = flask.Blueprint("feedback", __name__, url_prefix="/feedback")


@feedback_bp.route("/ses/", methods=["POST", "GET"])
def ses():
    # AWS sends JSON with text/plain mimetype
    try:
        feedback_data = json.loads(flask.request.data)
    except ValueError:
        pass

    sns_message_type = flask.request.headers.get("X-Amz-Sns-Message-Type")

    # Subscribe to the SNS topic
    if sns_message_type == "SubscriptionConfirmation" and "SubscribeURL" in feedback_data:
        requests.get(feedback_data["SubscribeURL"])

    # TODO: handle bounces and complaints properly

    return "", 200
