from app import db
from app.users import users
from app.users.models import User
# from forms import LoginForm, RequestResetForm, ResetPasswordForm, EditUserForm, AddUserForm
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
    
    return render_template('user_page.html')