from app import db
from app.campaigns import campaigns
from app.users.models import User
from app.campaigns.models import Campaign
from app.campaigns.forms import CreateCampaignForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import os
from time import sleep

@campaigns.route('add_campaign', methods=['GET', 'POST'])
def add_campaign():
    form = CreateCampaignForm()
    if form.validate_on_submit():
        campaign = Campaign(
            title=form.title.data,
            active=form.active.data,
            goal=form.goal.data
        )
        db.session.add(campaign)
        db.session.commit()
        return redirect(url_for('admin.administration'))
    return render_template('add_campaign.html',
                           form=form)

@campaigns.route('campaign_page/<campaign_id>')
def campaign_page(campaign_id):
    campaign = Campaign.query.filter_by(id=campaign_id).first()
    return render_template('campaign_page.html',
                           campaign=campaign)

@campaigns.route('add_ambassador')
def add_ambassador():
    return render_template('add_ambassador.html')