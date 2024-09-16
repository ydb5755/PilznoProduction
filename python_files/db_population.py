from sqlalchemy import create_engine, MetaData, Table, select, insert, func, update, bindparam, delete
import os
import csv
from datetime import datetime, timedelta
from dateutil.parser import parse
import time
import json
from werkzeug.security import generate_password_hash
import random
def engineer():
    engine = create_engine('sqlite:////home/yisroel2/Desktop/Pilzno/instance/site.db')
    # engine = create_engine('sqlite:///C:/Users/Lenovo/Desktop/Pilzno/instance/site.db')
    metadata_obj = MetaData()
    metadata_obj.reflect(bind=engine)
    return engine, metadata_obj



def insert_users():
    users = [
        ['Yisroel', 'Baum', 'yisroel.d.baum@gmail.com', generate_password_hash('12'), 'Admin'],
        ['Yoni', 'Gerzi', 'yoni@gerzi.com', generate_password_hash('12'), 'User'],
        ['Shmuli', 'Modes', 'shmuli@modes.com', generate_password_hash('12'), 'User'],
        ['Emma', 'Baum', 'emma@baum.com', generate_password_hash('12'), 'User'],
        ['Yisroel', 'Factor', 'yisroel@factor.com', generate_password_hash('12'), 'User'],
        ['Yaakov', 'Frager', 'yaakov@frager.com', generate_password_hash('12'), 'User'],
        ['Michael', 'Oshman', 'michael@oshman.com', generate_password_hash('12'), 'User'],
        ['Shalom', 'Goldberg', 'shalom@goldberg.com', generate_password_hash('12'), 'User'],
        ['Daniel', 'Caller', 'daniel@caller.com', generate_password_hash('12', 'User')],

    ]
    engine, metadata_obj = engineer()
    user_table = Table("user", metadata_obj, autoload_with=engine)
    
    with engine.connect() as conn:
        for user in users:
            conn.execute(user_table.insert().values(
                first_name = user[0],
                last_name = user[1],
                email = user[2],
                password = user[3],
                user_type = user[4]
            ))
        conn.commit()

def insert_donations():
    engine, metadata_obj = engineer()
    donation_table = Table("donation", metadata_obj, autoload_with=engine)

    currency_types = ['shekel', 'dollar']
    
    with engine.connect() as conn:
        for _ in range(100):
            conn.execute(donation_table.insert().values(
                currency_type = currency_types[random.randint(1,2)],
                amount = random.randint(1,200),
                campaign_id=1,
                user_id=1
            ))
        conn.commit()

def insert_campaigns():
    engine, metadata_obj = engineer()
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)

    campaign_titles = ['general campaign', 'yomim noraim 2024', 'pesach kibbudim 2024', 'RH kibbudim 2024']
    with engine.connect() as conn:
        for title in campaign_titles:
            conn.execute(campaign_table.insert().values(title=title))
        conn.commit()

def test_selections():
    engine, metadata_obj = engineer()
    user_table = Table("user", metadata_obj, autoload_with=engine)
    donation_table = Table("donation", metadata_obj, autoload_with=engine)
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)

    for x in range(10):
        print(random.randrange(1,4))
    # with engine.connect() as conn:
    #     campaign_one = conn.execute(select(campaign_table).where(campaign_table.c.id==1)).first()
    #     donation_one = conn.execute(select(donation_table).where(donation_table.c.id==1)).first()
    #     user_one = conn.execute(select(user_table).where(user_table.c.id==1)).first()
    #     print(user_one)

def delete_all():
    engine, metadata_obj = engineer()
    user_table = Table("user", metadata_obj, autoload_with=engine)
    donation_table = Table("donation", metadata_obj, autoload_with=engine)
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)

    with engine.connect() as conn:
        conn.execute(delete(user_table))
        conn.execute(delete(campaign_table))
        conn.execute(delete(donation_table))
        conn.commit()

def insert_all():
    insert_users()
    insert_campaigns()
    insert_donations()

if __name__ == '__main__':
    test_selections()
