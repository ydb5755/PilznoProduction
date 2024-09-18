from app import db
from app.main import main
from app.users.models import User
from app.campaigns.models import Campaign
# from forms import LoginForm, RequestResetForm, ResetPasswordForm, EditUserForm, AddUserForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import os
# import logging
# logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.INFO)


@main.route('/homepage')
def homepage():
    active_campaigns = Campaign.query.filter_by(active=True).all()
    return render_template('homepage.html',
                           active_campaigns=active_campaigns)