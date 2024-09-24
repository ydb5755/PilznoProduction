from flask import Blueprint

arba_yesodot = Blueprint('arba_yesodot', 
                     __name__, 
                     template_folder='templates', 
                     static_folder='static',
                     url_prefix='/arba_yesodot')

from app.arba_yesodot import routes