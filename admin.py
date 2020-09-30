from sqlalchemy import create_engine
from instance.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.orm import sessionmaker
from app.models import Employee

url = SQLALCHEMY_DATABASE_URI
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


def create_admin():
    admin = Employee(email="admin@gmail.com", username="admin",
                     password="admin123", is_admin=True)
    session.add(admin)
    session.commit()
    print("Admin data is entered.")
    print("Check Readme file for credentials.")


if __name__ == "__main__":
    create_admin()
