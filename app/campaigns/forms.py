from flask_wtf import FlaskForm
from wtforms import StringField, \
                    EmailField, \
                    PasswordField, \
                    SubmitField, \
                    SelectField, \
                    BooleanField,\
                    DateField, IntegerField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, ValidationError, NumberRange, EqualTo, Email
from app.campaigns.models import Campaign
from flask_login import current_user
# import logging
# logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)

class CreateCampaignForm(FlaskForm):
    title        = StringField('Title', validators=[DataRequired()])
    active       = BooleanField('Initialize as active?')
    goal         = IntegerField('Goal')
    submit       = SubmitField('Add Campaign')