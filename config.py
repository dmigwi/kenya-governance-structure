import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    TESTING = False

class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    TESTING = True