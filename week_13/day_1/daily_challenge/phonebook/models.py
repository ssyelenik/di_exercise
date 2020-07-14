from . import db

class Person(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64))
    email=db.Column(db.String,unique=True)
    phone_num=db.Column(db.String(10),unique=True)
    address=db.Column(db.Text)
