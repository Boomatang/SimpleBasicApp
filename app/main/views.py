from flask import render_template
from flask_login import login_required

from app.decorators import company_asset
from . import main


@main.route('/', methods=['POST', 'GET'])
def index():
    # TODO add a redirect to the main index page
    return render_template('main/index.html')


@main.route('/test')
@login_required
def test():
    return render_template('main/test.html')


@main.route('/test/<asset>')
@login_required
@company_asset()
def test_asset(asset):
    return render_template('main/test_token.html', asset=asset)
