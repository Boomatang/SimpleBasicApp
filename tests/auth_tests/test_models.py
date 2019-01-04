import pytest
from flask import url_for

from app import db
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


def test_valid_confirmation_token():
    u = User()
    u.password = 'cat'
    db.session.add(u)
    db.session.commit()

    token = u.generate_confirmation_token()

    assert u.confirm(token)
