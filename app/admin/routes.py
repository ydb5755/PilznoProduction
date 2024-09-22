from app import db
from app.admin import admin
from app.users.models import User
from app.campaigns.models import Campaign
from app.main.models import Donation
from app.users.forms import LoginForm, RegisterUserForm#, RequestResetForm, ResetPasswordForm, EditUserForm, AddUserForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import os

@admin.route('administration')
def administration():
    users = User.query.all()
    campaigns = Campaign.query.filter_by(archived=False).all()
    return render_template('administration.html',
                           users=users,
                           campaigns=campaigns)
