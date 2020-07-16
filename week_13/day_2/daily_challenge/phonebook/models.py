from . import db
from flask_sqlalchemy import SQLAlchemy


class Nationality(db.Model):

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64),unique=True)
    people=db.relationship('Person',backref='nat')

class Person(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64))
    email=db.Column(db.String,unique=True)
    phone_num=db.Column(db.String(10),unique=True)
    address=db.Column(db.Text)
    nat_id=db.Column(db.Integer,db.ForeignKey('nationality.id'))



