from flask import Flask
from flask_navigation import Navigation

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
