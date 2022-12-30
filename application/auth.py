from flask import Blueprint, render_template, flash, request, redirect, url_for
from .dataAccess import get_user_by_email, add_user, check_user_password
from flask_login import login_user, login_required, logout_user
from . import FLASH_ERROR, FLASH_SUCCESS

auth = Blueprint('auth', __name__)


def create_admin_user():
    user = get_user_by_email('admin@gmail.com')
    if not user:
        add_user("admin@gmail.com", "1234")
        print("admin user created!")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').strip()
        password = request.form.get('password')
        error = False
        if len(email) == 0:
            flash("Email is empty!", category=FLASH_ERROR)
            error = True

        if len(password) == 0:
            flash("Password is empty!", category=FLASH_ERROR)
            error = True
        if not error:
            user = get_user_by_email(email)
            if check_user_password(user, password):
                login_user(user, remember=True)
                return redirect(url_for("view.home"))
        flash("Unable to login!", category=FLASH_ERROR)

    return render_template("login.html", page_type='login')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successfully!', category='success')
    return redirect(url_for('auth.login'))


@auth.route('/add-new-user', methods=['GET', 'POST'])
@login_required
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        import re

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not re.fullmatch(regex, email):
            flash('Emtpy email address.', category=FLASH_ERROR)
        elif password1 != password2:
            flash('Password does not match!.', category=FLASH_ERROR)
        elif len(password1) < 4:
            flash('Password must be of minimum length 4')
        else:
            if not add_user(email, password1):
                flash('Email already exists', category=FLASH_ERROR)
            else:
                flash('User created successfully', category=FLASH_SUCCESS)
    return render_template("sign-up.html", page_type='register')
