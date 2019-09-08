from flask import render_template

from affo_email_service.models.message import message_schema
from affo_email_service.services import email_service


def send(template_name, message):
    message["html"] = render_template(f"email/{template_name}.html", **message["variables"])
    message["text"] = render_template(f"email/{template_name}.txt", **message["variables"])

    # FIXME: attachments aren't supported
    return (
        message_schema.jsonify(
            email_service.send(
                from_=message["from_"],
                to=message["to"],
                subject=message["subject"],
                text=message["text"],
                html=message["html"],
                tag=message["tag"],
                attachments=message.get("attachments", None),
            )
        ),
        201,
    )
