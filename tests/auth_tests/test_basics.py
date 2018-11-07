import pytest
from flask import current_app, url_for

paths = ['auth_tests.index']


def test_app_exists(client):
    assert client is not None


def test_app_is_testing(client):
    assert current_app.config['TESTING']


@pytest.mark.single_thread
@pytest.mark.parametrize('path', paths)
def test_main_nav_paths(client, path):

    assert client.get(url_for(path)).status_code == 200
