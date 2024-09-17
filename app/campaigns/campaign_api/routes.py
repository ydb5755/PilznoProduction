from flask import render_template
from app.campaigns.campaign_api import campaign_api


@campaign_api.route('testing')
def testing():
    return render_template('testing.html')