from hamcrest import *

from pytest_toolbelt import matchers


def test_unsubscribe(client):
    response = client.get('/api/v1.0/unsubscribe/test%40example.com/token/notification/')
    assert_that(response, matchers.has_status(200))

    response = client.get(path=f'/unsubscribe/{response.json["token"]}/')
    assert_that(response, matchers.has_status(200))

    response = client.post(
        '/api/v1.0/message/',
        json={
            'from_': 'test@example.com',
            'to': ['test@example.com'],
            'subject': 'Test',
            'html': '',
            'text': '',
            'tag': 'notification'
        }
    )
    assert_that(response, matchers.has_status(201))
    assert_that(
        response.data.decode(),
        matchers.is_json(
            has_entries('status', 'SKIPPED')
        )
    )
