from flask import Blueprint

users_api = Blueprint('users_api', 
                     __name__, 
                     template_folder='templates', 
                     static_folder='static',
                     url_prefix='/users_api')

from app.users.users_api import routes