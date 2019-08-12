from .utils import send_from_dict


def create(message):
    # FIXME: attachments aren't supported

    return send_from_dict(message), 201
