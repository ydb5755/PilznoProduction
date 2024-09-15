from app import db
from flask import current_app
from flask_login import UserMixin, current_user
from sqlalchemy import TEXT, Column, Boolean, ForeignKey, TEXT, INTEGER, VARCHAR
import jwt
from datetime import datetime, timezone, timedelta


class Donation(db.Model):
    __tablename__ = 'donation'
    id            = Column('id', INTEGER(), primary_key=True, autoincrement=True)
    currency_type = Column('currency_type', TEXT(), nullable=False)
    amount        = Column('amount', INTEGER(), nullable=False)
    campaign      = db.relationship('campaign', backref='donation', lazy='dynamic')
    user          = db.relationship('user', backref='donation', lazy='dynamic')