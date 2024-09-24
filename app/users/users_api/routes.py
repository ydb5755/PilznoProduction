from app import db
from flask import render_template
from app.users.users_api import users_api
from app.users.models import User
from time import sleep



@users_api.route('update_admin_status/<id>/<status>', methods=['PUT'])
def update_admin_status(id, status):
    if status == 'true':
        status = 'Admin'
    else:
        status = 'User'
    User.query.filter_by(id=id).update({'user_type':status})
    db.session.commit()
    sleep(1)
    return {'status':'success'}
