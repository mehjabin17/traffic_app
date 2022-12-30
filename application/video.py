from flask import Blueprint, render_template
from flask_login import login_required

video = Blueprint('video', __name__)


@video.route('/rtsp-stream')
@login_required
def play_video():
    return render_template("video.html")


@video.route('/video-analytics')
@login_required
def analytics():
    return render_template("video.html")


@video.route('/clips')
@login_required
def clips():
    return render_template("clips.html")
