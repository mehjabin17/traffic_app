from flask_login import current_user
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash

from .models import *


def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def check_user_password(user, password):
    return user and check_password_hash(user.password, password)


def add_user(email: str, password: str) -> bool:
    user = get_user_by_email(email)
    result = False
    if not user:
        user_id = None
        if current_user:
            user_id = current_user.id
        try:
            db.session.add(
                User(
                    email=email,
                    password=generate_password_hash(password, method='sha256'),
                    user_id=user_id
                )
            )
            db.session.commit()
            result = True
        except exc.SQLAlchemyError:
            db.session.rollback()
    return result
