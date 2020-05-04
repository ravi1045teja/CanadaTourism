import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base 54.162.179.234
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:Qwerty@1@54.162.179.234/cloud_auth'
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:kutty007@localhost/cloud_auth' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        'users': 'mysql+pymysql://user:Qwerty@1@54.162.179.234/cloud_db',
        #'users': 'mysql://root:kutty007@localhost/cloud_db',
        'aut': SQLALCHEMY_DATABASE_URI
    }

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:kutty007@localhost/flask' 
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base

class MainDB(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:kutty007@localhost/internship_portal' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig,
    main=MainDB
)

key = Config.SECRET_KEY