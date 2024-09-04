from app import db
from flask import current_app
from flask_login import current_user
from sqlalchemy import TEXT, Column, Boolean, ForeignKey, TEXT, INTEGER, VARCHAR
import jwt
from datetime import datetime, timezone, timedelta



class Campaign(db.Model):
    __tablename__ = 'campaign'
    id         = Column('id', INTEGER(), primary_key=True)
    title = Column('title', TEXT(), nullable=False)
    email      = Column('email', TEXT(), nullable=False, unique=True)
    password   = Column('password', TEXT(), nullable=False)
    user_type  = Column('user_type', TEXT(), nullable=False)