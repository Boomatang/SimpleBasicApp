from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, Length, Email, Regexp, EqualTo, ValidationError

from app.auth_models import User


class LoginForm(FlaskForm):
    email = StringField('E-mail address', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    remember_me = BooleanField('Keep me logged in')

    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('E-mail address', validators=[data_required(), Length(1, 64),
                                                      Email()])
    username = StringField('Username', validators=[
        data_required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                               'Username\'s must have only letters, '
                                               'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        data_required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[data_required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[data_required()])
    password = PasswordField('New password', validators=[
        data_required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[data_required()])
    submit = SubmitField('Update Password')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[data_required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[data_required(), Length(1, 64),
                                             Email()])
    password = PasswordField('New Password', validators=[
        data_required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[data_required()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')


class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[data_required(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Password', validators=[data_required()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
