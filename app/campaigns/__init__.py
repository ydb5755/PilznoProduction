from flask import Blueprint

campaigns = Blueprint('campaigns', 
                     __name__, 
                     template_folder='templates', 
                     static_folder='static',
                     url_prefix='/campaigns')

from app.campaigns import routes