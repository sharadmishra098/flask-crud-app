# Flask Toy Project
A CRUD application Employee Management System using flask.

## Built Using
* HTML
* CSS
* Bootstrap
* Python3
* Flask
* Flask-SQLAlchemy

## Create Virtual environment
1. Install virual environment
   > pip install virtualenv
2. Create a virual environment
   > virtualenv environment_name
3. Activate the virual environment
   > source environment_name/bin/activate

## Install the requiremnts
> pip install -r requirements.txt

## Run the Project
1. Set Username and password in instance/config.py file
2. Create Database
   > python3 create_db.py
3. Create the tables
   > flask db upgrade
4. Run admin.py file to create an admin.
   > python3 admin.py
5. Run the flask server
   > flask run
6. Go to the link generated in above step. \
   To log in as admin:
   > email: admin@gmail.com \
   > password: admin123
7. To delete the database
   > python3 delete_db.py
8. Deactivate the virtual environment
   > deactivate

# Author
Sharad Mishra - _sharad.mishra@mountblue.tech_