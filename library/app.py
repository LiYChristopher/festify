#creates the app and can include a config.py

from flask import Flask

def create_app(config=None, app_name=None, blueprints=None):
    app = Flask(__name__)
    return app

app = create_app()