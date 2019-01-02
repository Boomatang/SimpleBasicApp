import pytest
from flask import current_app, url_for

from app import db
from app.auth_models import User

paths = ['main.index', 'auth.login', 'auth.register']


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
    u = User()
    u.email = user['email']
    u.password = user['password']
    db.session.add(u)
    db.session.commit()
    data = {'email': user['email'],
            'password': user['password']}
    response = client.post(url_for('auth.login'),
                           data=data, follow_redirects=True)

    assert b'<h1>Page Header</h1>' in response.data


users = [{'email': 'fail1@example.com', 'password': 'fake'}]


@pytest.mark.parametrize('user', users)
def test_user_login_fails(client, user):
    data = {'email': user['email'],
            'password': user['password']}
    response = client.post(url_for('auth.login'),
                           data=data, follow_redirects=True)

    assert b'Invalid E-mail or Password' in response.data


users = [{'username': 'jim', 'email': 'jim@test.com', 'password': 'cat', 'password2': 'cat'}]


@pytest.mark.parametrize('user', users)
def test_user_register_complete(clean_db, client, user):
    data = {'username': user['username'],
            'email': user['email'],
            'password': user['password'],
            'password2': user['password2']}

    response = client.post(url_for('auth.register'),
                           data=data)

    assert response.status_code == 302


users = [{'username': 'jim fitz', 'email': 'test@test.com', 'password': 'cat', 'password2': 'cat',
          'massage': b'must have only letters'},
         {'username': 'jim', 'email': 'jim@test', 'password': 'cat', 'password2': 'cat',
          'massage': b'Invalid email address'},
         {'username': 'jim', 'email': 'jim@test.com', 'password': 'cat', 'password2': 'dog',
          'massage': b'Passwords must match'}]


@pytest.mark.parametrize('user', users)
def test_user_register_fails(clean_db, client, user):
    data = {'username': user['username'],
            'email': user['email'],
            'password': user['password'],
            'password2': user['password2']}

    response = client.post(url_for('auth.register'),
                           data=data)

    assert user['massage'] in response.data
