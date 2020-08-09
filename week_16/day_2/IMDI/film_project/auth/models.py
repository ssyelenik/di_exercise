import flask_login
from flask_login import UserMixin

from .. import db, login_mgr

@login_mgr.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    users=db.relationship('User',backref='permission')



# First - Create a class that inherit from db.Model
class User(db.Model, UserMixin):

    # Second - Create your model's columns
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(64))
    email    = db.Column(db.String(132))
    password = db.Column(db.String(512))
    my_role    = db.Column(db.Integer,db.ForeignKey('role.id'))

    def set_password(self, pwd):
        self.password = pwd

    def check_password(self, pwd):
        return self.password == pwd

    def send_reset_pwd_mail(self):
            payload = {
                'user_id': self.id,
                'expires': (datetime.datetime.now() + datetime.timedelta(hours=2)).timestamp()
            }

            token = jwt.encode(payload, app.config["SECRET_KEY"])

            url = flask.url_for('main.reset_password', jwt_token=token, _external=True)
            # Create a mail
            msg = flask_mail.Message(
                subject="Password Reset",
                recipients=[self.email],
                body=f"Hello {self.name}, to reset your password, navigate to {url}",
                sender=app.config["MAIL_USERNAME"]
            )

            # Send it !
            mail_mgr.send(msg)

    def follow(self, user_id):
        if user_id == self.id:
            return True

        user = User.query.get(user_id)


        if not user:
            flask.abort(404)

        self.following.append(user)

        db.session.commit()


    @classmethod
    def authenticate(cls, mail, password):
        user = cls.query.filter_by(email=mail).first()

        if user is not None and user.check_password(password):
            flask_login.login_user(user)
            return user


    def __repr__(self):
        return f"<User {self.name}>"
