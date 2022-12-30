from flask import Flask

SECRET_KEY = "The World is not Enough"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    return app
