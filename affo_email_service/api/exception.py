import http

import connexion_buzz


class NoSuchMessage(connexion_buzz.ConnexionBuzz):
    status_code = http.HTTPStatus.NOT_FOUND
