import itsdangerous

from affo_email_service import settings


def token(email, tag):
    safe = itsdangerous.URLSafeTimedSerializer(settings.SECRET_KEY)

    return {"token": safe.dumps({"email": email, "tag": tag})}, 200
