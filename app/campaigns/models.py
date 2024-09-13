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
    donation_id = Column(INTEGER, ForeignKey('donation.id'))
    #ambassadors 