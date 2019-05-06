# SimpleBasicAPP

This is app is used by a college assignment to shown how a week site can be attacked.

In the .env file the following settings can be added.
- APP\_Config=simple

  This puts the app in a simple form or in HTTP mode

- APP\_Config=TLS

  This puts the app in a secure mode or in HTTPS mode. You will require certs for this to work.
- APP\_Config=XSS

  In this configuration the app allows cross site scripting to happen.

To install the app dependencies using pipenv:
**pipenv install**

To run the app using pipenv call:
**pipenv run python app.py**


