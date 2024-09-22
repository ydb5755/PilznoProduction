from app import db
from flask import current_app
from flask_login import current_user
from sqlalchemy import TEXT, Column, Boolean, ForeignKey, TEXT, INTEGER, VARCHAR
import jwt
from datetime import datetime, timezone, timedelta


class AmbassadorMap(db.Model):
    __tablename__ = 'ambassador_map'
    id            = Column('id', INTEGER(), primary_key=True)
    campaign_id   = Column('campaign_id', INTEGER(), nullable=False)
    user_id       = Column('user_id', INTEGER(), nullable=False)



class Campaign(db.Model):
    __tablename__ = 'campaign'
    id            = Column('id', INTEGER(), primary_key=True)
    title         = Column('title', TEXT(), nullable=False)
    active        = Column('active', Boolean(), nullable=False, default=True)
    goal          = Column('goal', INTEGER(), default=0)
    archived      = Column('archived', Boolean(), default=False)

    def get_donations(self):
        from app.main.models import Donation
        return Donation.query.filter_by(campaign_id=self.id).all()


    def __repr__(self) -> str:
        return f"{self.id} - {self.title}"
    # donation_id = Column(INTEGER, ForeignKey('donation.id'))