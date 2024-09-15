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
    donations = db.relationship('Donation', backref='campaign', lazy='dynamic')

    def __repr__(self) -> str:
        return f"{self.id} - {self.title}"
    # donation_id = Column(INTEGER, ForeignKey('donation.id'))