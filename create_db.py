"""This file is to create database if it doesn't exist"""

from sqlalchemy import create_engine
from instance.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy_utils import create_database, database_exists


def make_db():
    """Function to create database"""
    url = SQLALCHEMY_DATABASE_URI
    engine = create_engine(url)
    if not database_exists(engine.url):
        create_database(engine.url)
    if database_exists(engine.url):
        print("Database created successfully")


if __name__ == "__main__":
    make_db()
