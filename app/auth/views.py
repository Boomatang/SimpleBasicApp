from flask_login import current_user, login_user, login_required, logout_user

from app import db
from app.auth import auth
from flask import render_template, url_for, redirect, request, flash
from app.auth.forms import LoginForm, RegistrationForm
from app.auth_models import User


@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint[:5] != 'auth.':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        form.email.errors.append('Invalid E-mail or Password')
        form.password.errors.append('Invalid E-mail or Password')
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data

        user = User(email=email, username=username)
        user.password = form.password.data

        db.session.add(user)

        db.session.commit()
        flash('You have been signed up. Please login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

