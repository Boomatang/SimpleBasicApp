from flask import render_template, redirect, url_for
from flask_login import login_required

from app import db
from app.auth_models import Comment
from app.main.forms import CommentForm
from . import main


@main.route('/', methods=['POST', 'GET'])
def index():
    # TODO add a redirect to the main index page
    return render_template('main/index.html')


@main.route('/test')
@login_required
def test():
    return render_template('main/test.html')


@main.route('/css', methods=['POST', 'GET'])
def cross_site_scripting():
    form = CommentForm()

    comments = Comment.query.all()[:]

    if form.validate_on_submit():

        new_comment = form.comment.data

        comment = Comment(comment=new_comment)

        db.session.add(comment)
        db.session.commit()

        print('Message')

        return redirect(url_for('main.cross_site_scripting'))

    return render_template('main/css.html', form=form, comments=comments)


@main.route('/simple_form', methods=['POST', 'GET'])
def simple_form():

    return render_template('main/simple.html')
