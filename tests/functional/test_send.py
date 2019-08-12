from hamcrest import *

import pytest

from pytest_toolbelt import matchers

from affo_email_service.extensions import mail


@pytest.mark.parametrize('message', [
    {
        'from_': 'from@example.com',
        'to': ['to@example.com'],
        'subject': 'Hello',
        'html': '',
        'text': '',
        'tag': 'test'
    }
])
def test_send(client, message):
    with mail.record_messages() as outbox:
        response = client.post(
            '/api/v1.0/message/',
            json={
                'from_': 'from@example.com',
                'to': ['to@example.com'],
                'subject': 'Hello',
                'html': '',
                'text': '',
                'tag': 'test'
            }
        )
        assert_that(response, matchers.has_status(201))

        assert_that(
            outbox[0],
            has_properties(
                subject='Hello',
                sender=message['from_'],
                recipients=message['to']
            )
        )
