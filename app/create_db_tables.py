""" This file holds the schemas to create new tables on database, if necessary.
To create a table change the table value in function on line 51 and run file.
This code should not have to be run unless new (empty) tables have to be generated.
"""
import os

import psycopg2
from dotenv import load_dotenv


def initialize_police_table():
    load_dotenv()
    # police_table = """CREATE TABLE IF NOT EXISTS police_force (
    # id SERIAL PRIMARY KEY NOT NULL,
    # dates TIMESTAMP,
    # links TEXT,
    # case_id TEXT,
    # city TEXT,
    # state TEXT,
    # title TEXT,
    # description TEXT,
    # tags TEXT,
    # force_rank TEXT,
    # confidence TEXT
    #     );"""

    pi_table = """CREATE TABLE IF NOT EXISTS twitter_incidents (
    incident_id SERIAL PRIMARY KEY NOT NULL,
    date_created TIMESTAMP,
    tweet_id TEXT,
    user_name TEXT,
    description VARCHAR(10000),
    city TEXT,
    state TEXT,
    lat FLOAT,
    long FLOAT,
    title TEXT,
    force_rank TEXT,
    status TEXT,
    confidence FLOAT,
    tags TEXT
          );"""
    
    db_url = os.getenv('DB_URI')
    conn = psycopg2.connect(db_url)
    curs = conn.cursor()
    curs.execute(pi_table)
    conn.commit()
    curs.close()
    conn.close()

