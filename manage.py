import os

from app import create_app

app = create_app(os.getenv('APP_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db='This is db')


if __name__ == '__main__':
    app.run()
