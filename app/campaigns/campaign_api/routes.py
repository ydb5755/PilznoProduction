from app import db
from flask import render_template
from app.campaigns.campaign_api import campaign_api
from app.campaigns.models import Campaign
from time import sleep



@campaign_api.route('update_active_status/<id>/<status>', methods=['PUT'])
def update_active_status(id, status):
    if status == 'true':
        status = True
    else:
        status = False
    Campaign.query.filter_by(id=id).update({'active':status})
    db.session.commit()
    sleep(1)
    return {'status':'success'}

@campaign_api.route('archive_campaign/<id>', methods=['PUT'])
def archive_campaign(id):
    Campaign.query.filter_by(id=id).update({'archived': True, 'active':False})
    db.session.commit()
    return {'status':'success'}