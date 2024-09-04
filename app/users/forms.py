from flask_wtf import FlaskForm
from wtforms import StringField, \
                    EmailField, \
                    PasswordField, \
                    SubmitField, \
                    SelectField, \
                    BooleanField,\
                    DateField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, ValidationError, NumberRange, EqualTo, Email
from app.users.models import User
from flask_login import current_user
# import logging
# logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)

class LoginForm(FlaskForm):
    email        = EmailField('Email', validators=[DataRequired()])
    password     = PasswordField('Password', validators=[DataRequired()])
    remember     = BooleanField('Remember me')
    submit       = SubmitField('Login')

class RegisterUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password  = StringField('Password', validators=[DataRequired()])
    confirm_password  = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')