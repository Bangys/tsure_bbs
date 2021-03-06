from flask import session

from app.models.user import User


def current_user():
    uid = session.get('user_id', -1)
    u = User.query.filter_by(id=uid).first()
    return u
