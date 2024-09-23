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
from time import sleep

@campaigns.route('add_campaign')
def add_campaign():
    return render_template('add_campaign.html')

@campaigns.route('campaign_page/<campaign_id>')
def campaign_page(campaign_id):
    campaign = Campaign.query.filter_by(id=campaign_id).first()
    return render_template('campaign_page.html',
                           campaign=campaign)

@campaigns.route('update_active_status/<id>/<status>', methods=['PUT'])
def update_active_status(id, status):
    if status == 'true':
        status = True
    else:
        status = False
    Campaign.query.filter_by(id=id).update({'active':status})
    db.session.commit()
    sleep(1)
    return {'status':'success'}

@campaigns.route('archive_campaign/<id>', methods=['PUT'])
def archive_campaign(id):
    Campaign.query.filter_by(id=id).update({'archived': True, 'active':False})
    db.session.commit()
    return {'status':'success'}