from app import db
from app.admin import admin
from app.users.models import User
from app.users.forms import LoginForm, RegisterUserForm#, RequestResetForm, ResetPasswordForm, EditUserForm, AddUserForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import os

@admin.route('administration')
def administration():
    return render_template('administration.html')
