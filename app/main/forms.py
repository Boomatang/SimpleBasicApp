from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField


class CommentForm(FlaskForm):
    comment = TextAreaField(label="Enter Comment")
    submit = SubmitField(label="Submit Comment")
