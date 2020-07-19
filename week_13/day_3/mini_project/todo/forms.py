from flask_wtf import FlaskForm
import wtforms
import flask

class Index(FlaskForm):
    todo_text=wtforms.StringField("Todo")
    submit=wtforms.SubmitField("Save New Todo")


class TodoComplete(FlaskForm):
    complete=wtforms.SubmitField("Mark as Complete")
    incomplete=wtforms.SubmitField("Mark as Incomplete")