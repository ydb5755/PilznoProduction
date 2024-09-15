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
    
    user_id = Column(INTEGER, ForeignKey('user.id'))
    campaign_id = Column(INTEGER, ForeignKey('campaign.id'))
    
    def __repr__(self) -> str:
        return f"{self.id} - {self.currency_type} - {self.amount}"
    # campaign      = db.relationship('Campaign', backref='donation', lazy='dynamic')
    # user          = db.relationship('User', backref='donation', lazy='dynamic')