from flask import url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user

from . import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def confirm(token):
        home_page = 'main.index'
        if current_user.confiremed:
            return redirect(url_for(home_page))
        if current_user.confirm(token):
            flash('You have confirmed your account. Thanks!')
        else:
            flash('The confirmation link is invalid or has expired')
        return redirect(url_for(home_page))
