from app import db
from app.arba_yesodot import arba_yesodot
from app.users.models import User
from app.campaigns.models import Campaign
from app.campaigns.forms import CreateCampaignForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import os
from time import sleep

@arba_yesodot.route('arba_yesodot_homepage')
def arba_yesodot_homepage():
    return render_template('arba_yesodot_homepage.html')