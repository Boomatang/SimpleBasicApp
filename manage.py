#!/usr/bin/env python
import os

from app import create_app, db
from flask_script import Manager, Shell
from app.auth_models import User

app = create_app(os.getenv('APP_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))


def set_up():
    db.create_all()


@manager.command
def sample_data():
    set_up()

    user1 = User(username='User1', email='user1@example.com', password='cat', confirmed=True)
    user2 = User(username='User2', email='user2@example.com', password='cat', confirmed=True)

    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

    print("Added sample data to database")


if __name__ == '__main__':
    manager.run()
