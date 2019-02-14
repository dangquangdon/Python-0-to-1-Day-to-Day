import os


# add the export below to .bashrc if you're on Mac or Linux
# export SECRET_KEY="201ee3b4c2d3bae27fc157a4eb9e9561"

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskapp.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
