import flask
from . import db
from . import app
from . import todo_class
from . import models
from . import forms

@app.route("/", methods=['GET','POST'])
def index():
    form=forms.Index()
    todo_obj=todo_class.Todo()
    todo_list=todo_obj.get_todos()
    if flask.request.method=="POST":
        todo_text=form.todo_text.data
        todo_new=todo_class.Todo(todo_text)
        todo_new.save_to_db()
        return flask.redirect(flask.url_for('index'))
    return flask.render_template("index.html",form=form,todo_list=todo_list)

@app.route("/complete", methods=['GET','POST'])
def complete():
    todo_list=models.Todolist.query.filter_by(is_todo_complete=None).all()
    print(todo_list)
    if todo_list=="":
        flask.flash("All of your todo items are already marked complete.")
        return flask.redirect(flask.url_for("index.html"))
    return flask.render_template("complete.html",todo_list=todo_list)


@app.route("/confirm/<todo_text>", methods=['GET','POST'])
def confirm(todo_text):

    form=forms.TodoComplete()

    return flask.render_template("confirm.html",form=form,todo_text=todo_text)

@app.route("/confirmed", methods=['GET','POST'])
def confirmed():
    todo_text=flask.request.form['todo_text']
    try:
        flask.request.form['complete']
        todo_record=models.Todolist.query.filter_by(todo_text=todo_text).first()
        todo_record.is_todo_complete=True
        db.session.commit()
        flask.flash(f'{todo_text} was marked as done.')
    except:
        flask.flash(f'{todo_text} is not done yet.')

    return flask.render_template("confirmed.html")






