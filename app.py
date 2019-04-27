import os

from config import config
from manage import app

app.run(ssl_context=config[os.getenv('APP_CONFIG') or 'default'].APP_SSL_CONTEXT)
