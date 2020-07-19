from . import db
from flask_sqlalchemy import SQLAlchemy

class Todolist(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    todo_text=db.Column(db.Text,unique=True)
    is_todo_complete=db.Column(db.Boolean)
    image_id=db.Column(db.Integer,db.ForeignKey('image.id'))
    categories=db.Column(db.Integer,db.ForeignKey('category.id'))

class Image(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    url=db.Column(db.String,unique=True)
    images=db.relationship('Todolist',backref='im',uselist=False)

class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True)
    todo=db.relationship('Todolist',backref='cat')