from . import db
from flask_login import UserMixin
from . import login_mngr

@login_mngr.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(64),unique=True)
    type = db.Column(db.String(5))
