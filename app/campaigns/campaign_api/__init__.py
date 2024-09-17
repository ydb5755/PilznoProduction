from flask import Blueprint

campaign_api = Blueprint('campaign_api', 
                     __name__, 
                     template_folder='templates', 
                     static_folder='static',
                     url_prefix='/campaign_api')

from app.campaigns.campaign_api import routes