from . import models
from . import app
from . import db

class Todo():
    todo_text=None
    todo_complete=None
    def __init__(self,todo=None):
        Todo.todo_text=todo
        Todo.todo_complete=None


    def get_todos(self):
        all_todos=models.Todolist.query.all()
        return all_todos

    def save_to_db(self):
        todo_record=models.Todolist(todo_text=Todo.todo_text,is_todo_complete=None)
        db.session.add(todo_record)
        db.session.commit()