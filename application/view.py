from flask import Blueprint, render_template, flash

view = Blueprint('view', __name__)


@view.route('/')
def home():
    return render_template("home.html")


@view.route('/settings')
def settings():
    return render_template("settings.html")
