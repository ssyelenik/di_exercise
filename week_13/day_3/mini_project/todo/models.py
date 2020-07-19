from . import db
from flask_sqlalchemy import SQLAlchemy

class Todolist(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    todo_text=db.Column(db.Text,unique=True)
    is_todo_complete=db.Column(db.Boolean)