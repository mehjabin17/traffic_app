from flask import Blueprint, render_template

video = Blueprint('video', __name__)


@video.route('/rtsp-stream')
def play_video():
    return render_template("video.html")


@video.route('/video-analytics')
def analytics():
    return render_template("video.html")


@video.route('/clips')
def clips():
    return render_template("clips.html")
