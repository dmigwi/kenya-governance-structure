class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////:memory:'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False

class TestConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True