import pytest
from flask import url_for

from app.auth_models import User


def test_user_password_setter():
    u = User()
    u.password = 'cat'
    assert u.password_hash is not None


def test_user_no_password_getter():
    u = User()
    u.password = 'cat'
    with pytest.raises(AttributeError):
        b = u.password


def test_user_password_verification():
    u = User()
    u.password = 'cat'
    assert u.verify_password('cat')
    assert not u.verify_password('dog')


def test_user_salts_are_random():
    u = User()
    u.password = 'cat'
    u2 = User()
    u2.password = 'cat'

    assert u.password_hash != u2.password_hash


paths = ['main.test']


@pytest.mark.single_thread
@pytest.mark.parametrize('path', paths)
def test_login_required(client, path):
    u = User()
    u.password = 'cat'
    u.email = 'test@test.test'

    response = client.post(url_for('auth.login'),
                           data={
                               'email': 'test@test.com',
                               'password': 'cat'},
                           follow_redirects=True)

    assert client.get(url_for(path), follow_redirects=True).status_code == 200
