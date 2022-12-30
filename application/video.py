from flask import Blueprint, render_template

video = Blueprint('video', __name__)


@video.route('/play')
def play_video():
    pass
