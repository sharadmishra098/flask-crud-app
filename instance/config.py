# instance/config.py
username = 'user1'
password = '123'
SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'postgresql://'+username+':'+password\
                            + '@localhost:5432/emp_db'
