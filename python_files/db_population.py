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
    path1 = 'C:/Users/Lenovo/Desktop/Pilzno/instance/site.db'
    path2 = '/home/yisroel2/Desktop/Pilzno/instance/site.db'
    path3 = '/home/ubuntu/PilznoProject/PilznoProduction/instance/site.db'

    for p in [path1, path2, path3]:
        if os.path.exists(p):
            path = p
            break
    engine = create_engine(f'sqlite:///{path}')
    metadata_obj = MetaData()
    metadata_obj.reflect(bind=engine)
    return engine, metadata_obj

def check_db():
    engine, metadata_obj = engineer()
    user_table = Table("user", metadata_obj, autoload_with=engine)
    donation_table = Table("donation", metadata_obj, autoload_with=engine)
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)
    with engine.connect() as conn:
        print('USERS')
        users = conn.execute(select(user_table)).all()
        if users:
            for user in users:
                print(user.first_name)
        else:
            print('no users')
        print("DONATIONS")
        donations = conn.execute(select(donation_table)).all()
        if donations:
            for donation in donations:
                print(donation.id)
        else:
            print('no donations')
        campaigns = conn.execute(select(campaign_table)).all()
        print('CAMPAIGNS')
        if campaigns:
            for campaign in campaigns:
                print(campaign.title)
        else:
            print('no campaigns')

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
        ['Daniel', 'Caller', 'daniel@caller.com', generate_password_hash('12'), 'User'],

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
    boolean_choice = [True, False]

    with engine.connect() as conn:
        for _ in range(100):
            conn.execute(donation_table.insert().values(
                currency_type = currency_types[random.randint(0,1)],
                amount = random.randint(1,200),
                anonymous = boolean_choice[random.randint(0,1)],
                campaign_id=random.randint(1,4),
                user_id=random.randint(1,9)
            ))
        conn.commit()

def insert_campaigns():
    engine, metadata_obj = engineer()
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)

    campaign_titles = ['general campaign', 'yomim noraim 2024', 'pesach kibbudim 2024', 'RH kibbudim 2024']
    is_active = [True, False]
    with engine.connect() as conn:
        for title in campaign_titles:
            conn.execute(campaign_table.insert().values(
                title=title,
                active=is_active[random.randint(0,1)],
                goal=5000, 
                archived=False
                ))
        conn.commit()

def insert_ambassador_relationships():
    engine, metadata_obj = engineer()
    user_table = Table("user", metadata_obj, autoload_with=engine)
    donation_table = Table("donation", metadata_obj, autoload_with=engine)
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)

    with engine.connect() as conn:
        campaign_ids = conn.execute(select(campaign_table.c.id)).all()
        user_ids = conn.execute(select(user_table.c.id)).all()


def test_selections():
    engine, metadata_obj = engineer()
    user_table = Table("user", metadata_obj, autoload_with=engine)
    donation_table = Table("donation", metadata_obj, autoload_with=engine)
    campaign_table = Table("campaign", metadata_obj, autoload_with=engine)


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
    delete_all()
    insert_all()
