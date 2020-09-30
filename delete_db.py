"""This file deletes the database if it exists."""

from sqlalchemy import create_engine
from instance.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy_utils import drop_database, database_exists


def drop_db():
    """Function to delete database"""
    url = SQLALCHEMY_DATABASE_URI
    engine = create_engine(url)
    if database_exists(engine.url):
        drop_database(engine.url)
        print("Database deleted")


if __name__ == "__main__":
    drop_db()
