import os


# add the export below to .bashrc if you're on Mac or Linux
# export SECRET_KEY="201ee3b4c2d3bae27fc157a4eb9e9561"

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = f'sqlite:////{os.path.join(os.getcwd(),"flaskapp.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True

MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
