import os
basedir = os.path.abspath(os.path.dirname(__file__))

# LOCAL DEV URI
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# REMOTE DEV URI
# SQLALCHEMY_DATABASE_URI = 'mysql://bounty:bvsupersecure@127.0.0.1:3306/bountyboard'
# BV FLYNN URI
SQLALCHEMY_DATABASE_URI = 'mysql://bounty:bvsupersecure@bountyboarddb.c182wh98aqxb.us-east-1.rds.amazonaws.com:3306/bountyboard'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SERVER_HOST_NAME = "127.0.0.1"
SERVER_PORT = 5000