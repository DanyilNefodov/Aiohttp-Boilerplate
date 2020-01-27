from sqlalchemy import create_engine, MetaData

from server.db import question, choice

import pathlib
import os

BASE_DIR = pathlib.Path(__file__).absolute().parent

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# db_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@/{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DSN = "postgres://postgres:postgres@0.0.0.0:5432/postgres"


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(question.insert(), [
        {'question_text': 'What\'s new?',
         'pub_date': '2015-12-15 17:17:49.629+02'}
    ])
    conn.execute(choice.insert(), [
        {'choice_text': 'Not much', 'votes': 0, 'question_id': 1},
        {'choice_text': 'The sky', 'votes': 0, 'question_id': 1},
        {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': 1},
    ])
    conn.close()


print(f"\n\n\n{db_url}\n\n\n")

if __name__ == '__main__':
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
