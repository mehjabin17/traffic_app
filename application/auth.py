from flask import Blueprint, render_template, flash

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    flash('Check Errror', category='error')
    flash('Check Succ', category='success')
    return render_template("login.html", page_type='login')


@auth.route('/logout')
def logout():
    pass


@auth.route('/add-new-user')
def sign_up():
    flash('Check Errror', category='error')
    flash('Check Succ', category='success')
    return render_template("sign-up.html", page_type='register')
