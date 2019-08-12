from flask import render_template

from .utils import send_from_dict


def send(template_name, message):
    message['html'] = render_template(f'email/{template_name}.html', **message['variables'])
    message['text'] = render_template(f'email/{template_name}.txt', **message['variables'])

    # FIXME: attachments aren't supported

    return send_from_dict(message), 201
