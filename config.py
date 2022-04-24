import os
from pickle import FALSE
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #setting the secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #setting the location of the db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False