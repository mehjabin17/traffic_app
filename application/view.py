from flask import Blueprint, render_template
from flask_login import login_required

view = Blueprint('view', __name__)


@view.route('/')
@login_required
def home():
    return render_template("home.html")


@view.route('/settings')
@login_required
def settings():
    return render_template("settings.html")
