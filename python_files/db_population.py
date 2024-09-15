from sqlalchemy import create_engine, MetaData, Table, select, insert, func, update, bindparam, delete
import os
import csv
from datetime import datetime, timedelta
from dateutil.parser import parse
import time
import json
from werkzeug.security import generate_password_hash



def insert_users():
    engine = create_engine('sqlite:///C:/Users/Lenovo/Desktop/Pilzno/instance/site.db')
    metadata_obj = MetaData()
    metadata_obj.reflect(bind=engine)
    user_table = Table("user", metadata_obj, autoload_with=engine)
    
    with engine.connect() as conn:
        conn.execute(user_table.insert().values(
            first_name = "Yisroel",
            last_name = "Baum",
            email = "yisroel.d.baum@gmail.com",
            password = generate_password_hash('12'),
            user_type = "User"
        ))
        conn.execute(user_table.insert().values(
            first_name = "Yoni",
            last_name = "Gerzi",
            email = "yoni@gerzi.com",
            password = generate_password_hash('12'),
            user_type = "User"
        ))
        conn.commit()

def insert_donations():
    engine = create_engine('sqlite:///C:/Users/Lenovo/Desktop/Pilzno/instance/site.db')
    metadata_obj = MetaData()
    metadata_obj.reflect(bind=engine)
    user_table = Table("user", metadata_obj, autoload_with=engine)
    donation_table = Table("donation", metadata_obj, autoload_with=engine)
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)

    with engine.connect() as conn:
        sruli = conn.execute(select(user_table).where(user_table.c.id == 1)).first()
        yoni = conn.execute(select(user_table).where(user_table.c.id == 2)).first()

        campaign_one = conn.execute(select(campaign_table).where(campaign_table.c.id == 2)).first()

        conn.execute(donation_table.insert().values(
            currency_type = "shekel",
            amount = 50,
            campaign_id=campaign_one.id,
            user_id=sruli.id
        ))
        conn.commit()

def insert_campaigns():
    engine = create_engine('sqlite:///C:/Users/Lenovo/Desktop/Pilzno/instance/site.db')
    metadata_obj = MetaData()
    metadata_obj.reflect(bind=engine)
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)

    with engine.connect() as conn:
        conn.execute(campaign_table.insert().values(title="general campaign"))
        conn.execute(campaign_table.insert().values(title="special campaign"))
        conn.commit()

def test_selections():
    engine = create_engine('sqlite:///C:/Users/Lenovo/Desktop/Pilzno/instance/site.db')
    metadata_obj = MetaData()
    metadata_obj.reflect(bind=engine)
    user_table = Table("user", metadata_obj, autoload_with=engine)
    donation_table = Table("donation", metadata_obj, autoload_with=engine)
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)

    with engine.connect() as conn:
        campaign_one = conn.execute(select(campaign_table).where(campaign_table.c.id==1)).first()
        donation_one = conn.execute(select(donation_table).where(donation_table.c.id==1)).first()
        user_one = conn.execute(select(user_table).where(user_table.c.id==1)).first()
        print(user_one.donations)

def delete_all():
    engine = create_engine('sqlite:///C:/Users/Lenovo/Desktop/Pilzno/instance/site.db')
    metadata_obj = MetaData()
    metadata_obj.reflect(bind=engine)
    user_table = Table("user", metadata_obj, autoload_with=engine)
    donation_table = Table("donation", metadata_obj, autoload_with=engine)
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)

    with engine.connect() as conn:
        conn.execute(delete(user_table))
        conn.execute(delete(campaign_table))
        conn.execute(delete(donation_table))
        conn.commit()

if __name__ == '__main__':
    test_selections()
