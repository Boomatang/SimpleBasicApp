from flask import Blueprint

auth = Blueprint('auth_tests', __name__)

from . import views
