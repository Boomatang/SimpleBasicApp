from app.auth import auth


@auth.route('/')
def index():
    return 'Hello World'
