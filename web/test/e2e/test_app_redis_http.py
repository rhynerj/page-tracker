# test/e2e/test_app_redis_http.py

import pytest
import requests


@pytest.mark.timeout(1.5)
def test_should_update_redis(redis_client, flask_url):
    # given
    redis_client.set('page_views', 4)

    # when
    response = requests.get(flask_url)

    # then
    assert response.status_code == 200
    assert response.text == 'This page has been seen 5 times.'
    assert redis_client.get('page_views') == b'5'
