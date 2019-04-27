from flask import render_template
from flask_login import login_required

from . import main


@main.route('/', methods=['POST', 'GET'])
def index():
    # TODO add a redirect to the main index page
    return render_template('main/index.html')


@main.route('/test')
@login_required
def test():
    return render_template('main/test.html')
