import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)


DEBUG = True
SECRET_KEY = config.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True

MAIL_USERNAME = config.get('MAIL_USERNAME')
MAIL_PASSWORD = config.get('MAIL_PASSWORD')
