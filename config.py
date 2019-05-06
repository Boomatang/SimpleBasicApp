import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    APP_SSL_CONTEXT = None

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TlsConfig(Config):
    SSL_DISABLE = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    # APP_SSL_CONTEXT = ("webserver.pem", "cert.pem")
    APP_SSL_CONTEXT = ('cert.pem', 'key.pem')


class XssConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    WTF_CSRF_ENABLED = False
    WTF_CSRF_METHODS = []
    SESSION_COOKIE_HTTPONLY = False
    REMEMBER_COOKIE_HTTPONLY = False
    SESSION_COOKIE_SECURE = False
    REMEMBER_COOKIE_SECURE = False


config = {
    'development': DevelopmentConfig,
    'XSS': XssConfig,
    'simple': DevelopmentConfig,
    'TLS': TlsConfig,

    'default': DevelopmentConfig
}
