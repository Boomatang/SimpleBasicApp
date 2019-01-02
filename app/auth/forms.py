from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import data_required


class LoginForm(FlaskForm):
    email = StringField('E-mail address', validators=[data_required()])
    password = PasswordField('Password', validators=[data_required()])
    submit = SubmitField('Login')
