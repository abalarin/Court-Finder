import os
import json
import urllib3
urllib3.disable_warnings()

with open(os.path.dirname(os.path.abspath(__file__)) + '/config.json') as config_file:
    config = json.load(config_file)


class Config:

    SECRET_KEY = os.urandom(12)

    DB_USER = config.get('DB_USER')
    DB_PASS = config.get('DB_PASS')

    # Connection to Postgres server
    SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASS + '@192.155.88.112:3306/courtfinder'

    # Set SQLAlchemy Connection Timeout Limits
    SQLALCHEMY_POOL_RECYCLE = 499
    SQLALCHEMY_POOL_TIMEOUT = 20


    # Gets pwd and declares it is the root dir for the App
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    #  boto3 Keys for Object Storage
    BOTO_KEY = config.get('BOTO_KEY')
    BOTO_SECRET = config.get('BOTO_SECRET')

    # Google Maps API
    GOOGLE_API_KEY = config.get('GOOGLE_API_KEY')

    # To suppress FSADeprecationWarning
    SQLALCHEMY_TRACK_MODIFICATIONS = False
