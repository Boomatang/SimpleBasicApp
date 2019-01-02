import pytest
from flask import current_app, url_for

paths = ['main.index', 'auth.login', 'auth.sign_up']


def test_app_exists(client):
    assert client is not None


def test_app_is_testing(client):
    assert current_app.config['TESTING']


@pytest.mark.single_thread
@pytest.mark.parametrize('path', paths)
def test_main_nav_paths(client, path):

    assert client.get(url_for(path)).status_code == 200




users = [{'email': 'pass1@example.com', 'password': 'cat'},
         {'email': 'pass2@example.com', 'password': 'cat'}]


@pytest.mark.parametrize('user', users)
def test_user_login_redirects_to_index(client, user):
    data = {'email': user['email'],
            'password': user['password']}
    response = client.post(url_for('auth.login'),
                           data=data, follow_redirects=True)

    assert b'<h1>Page Header</h1>' in response.data


users = [{'email': 'fail1@example.com', 'password': None}]


@pytest.mark.parametrize('user', users)
def test_user_login_fails(client, user):
    data = {'email': user['email'],
            'password': user['password']}
    response = client.post(url_for('auth.login'),
                           data=data, follow_redirects=True)

    assert b'Invalid E-mail or Password' in response.data
