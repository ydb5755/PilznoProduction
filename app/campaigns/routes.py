from app import db
from app.campaigns import campaigns
from app.users.models import User
from app.campaigns.models import Campaign
# from forms import LoginForm, RequestResetForm, ResetPasswordForm, EditUserForm, AddUserForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import os

@campaigns.route('add_campaign')
def add_campaign():
    return render_template('add_campaign.html')

@campaigns.route('campaign_page/<campaign_id>')
def campaign_page(campaign_id):
    campaign = Campaign.query.filter_by(id=campaign_id).first()
    return render_template('campaign_page.html',
                           campaign=campaign)