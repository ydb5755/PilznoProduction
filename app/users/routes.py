from app import db
from app.users import users
from app.users.models import User
from app.users.forms import LoginForm, RegisterUserForm#, RequestResetForm, ResetPasswordForm, EditUserForm, AddUserForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import os
# import logging
# logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.INFO)


@users.route('/user_page/<user_id>')
@login_required
def user_page(user_id):
    if not int(current_user.id) == int(user_id):
        return redirect(url_for('main.dashboard'))
    user = User.query.filter_by(id=user_id).first()
    return render_template('user_page.html',
                           user=user)


@users.route('/')
@users.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            flash('Please check your login details and try again.', 'bad')
            return redirect(url_for('users.login'))
        login_user(user, remember=form.remember.data)
        flash("You've been logged in successfully!", 'good')
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('main.homepage'))
    return render_template('login.html', 
                           form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You\'ve been successfully logged out!')
    return redirect(url_for('main.homepage'))

@users.route('/register_user', methods=('GET', 'POST'))
def register_user():
    form = RegisterUserForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
            user_type="User",
        )
        db.session.add(user)
        db.session.commit()
        flash('Succesfully Registered!')
        return redirect(url_for('main.homepage'))
    return render_template('register_user.html', form=form)