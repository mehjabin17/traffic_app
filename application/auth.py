from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    pass


@auth.route('/logout')
def logout():
    pass


@auth.route('/sign-up')
def sign_up():
    pass
