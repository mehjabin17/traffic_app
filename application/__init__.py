from flask import Flask
from flask_navigation import Navigation
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

db = SQLAlchemy()

SECRET_KEY = "The World is not Enough"
DB_NAME = "traffic.db"
FLASH_ERROR = "error"
FLASH_SUCCESS = "success"

password = b"malihamitu"
salt = os.urandom(16)


def get_fernet(fernet_pass, fernet_salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=fernet_salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(fernet_pass))
    return Fernet(key)


farnet = get_fernet(password, salt)


def initialize_db(app, drop=False, create=False):
    with app.app_context():
        if drop:
            db.drop_all()
        if create:
            db.create_all()
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # db code
    db.init_app(app)

    from .models import User
    initialize_db(app, True, True)

    # register login models and initialise Login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # register views
    from .view import view
    from .auth import auth
    from .video import video

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(video, url_prefix='/')

    # register menu items
    nav = Navigation(app)
    nav.Bar('sidebar', [
        nav.Item('Home', 'view.home', html_attrs={'icon': 'house-door', 'col_1': 9, 'col_2': 3}),
        nav.Item('Live', 'video.play_video', html_attrs={'icon': 'webcam', 'col_1': 9, 'col_2': 3}),
        nav.Item('Analytics', 'video.analytics', html_attrs={'icon': 'bar-chart-line', 'col_1': 9, 'col_2': 3}),
        nav.Item('Clips', 'video.clips', html_attrs={'icon': 'record', 'col_1': 7, 'col_2': 5}),
        nav.Item('Settings', 'view.settings', html_attrs={'icon': 'gear', 'no_mid_sect': True})
    ])

    return app
