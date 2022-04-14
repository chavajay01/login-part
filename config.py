class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:Root12345@localhost:3306/testdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 300
    SECRET_KEY = "horrible_secret_key"
    LOGIN_DISABLED = True
