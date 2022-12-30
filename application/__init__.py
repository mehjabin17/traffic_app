from flask import Flask

SECRET_KEY = "The World is not Enough"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    # register views
    from .view import view
    from .auth import auth
    from .video import video

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(video, url_prefix='/')

    return app
