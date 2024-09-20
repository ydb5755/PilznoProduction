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
    user_id       = Column('user_id', INTEGER(), nullable=False)
    campaign_id   = Column('campaign_id', INTEGER(), nullable=False)
    anonymous     = Column('anonymous', Boolean(), default=False)
    
    def get_user(self):
        from app.users.models import User
        return User.query.filter_by(id=self.user_id).first()

    def __repr__(self) -> str:
        return f"{self.id} - {self.currency_type} - {self.amount}"