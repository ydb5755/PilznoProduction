from app import db
from flask import current_app
from flask_login import UserMixin, current_user
from sqlalchemy import TEXT, Column, Boolean, ForeignKey, TEXT, INTEGER, VARCHAR
import jwt
from datetime import datetime, timezone, timedelta


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id         = Column('id', INTEGER(), primary_key=True)
    first_name = Column('first_name', TEXT(), nullable=False)
    last_name  = Column('last_name', TEXT(), nullable=False)
    email      = Column('email', TEXT(), nullable=False, unique=True)
    password   = Column('password', TEXT(), nullable=False)
    user_type  = Column('user_type', TEXT(), nullable=False)


    
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    # donation_id = Column(INTEGER, ForeignKey('donation.id'))
    
    def get_reset_token(self, expiration=600):
        reset_token = jwt.encode(
            {
                "confirm": self.id,
                "exp": datetime.now(tz=timezone.utc)
                       + timedelta(seconds=expiration)
            },
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )
        return reset_token
    
    @staticmethod
    def verify_reset_token(token):
        try:
            data = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                leeway=timedelta(seconds=10),
                algorithms=["HS256"]
            )
        except:
            return None
        if not User.query.get(data.get('confirm')):
            return None
        return User.query.get(data.get('confirm'))