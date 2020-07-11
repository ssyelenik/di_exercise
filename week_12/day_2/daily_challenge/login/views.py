from . import forms
import flask
import json
from . import app

import json
@app.route("/", methods=['GET','POST'])
def index():
    form = forms.MyForm()
    if flask.request.method=="POST":
        name=[flask.request.form['first_name'],flask.request.form['last_name']]
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letterf in name[0]:
            if letterf not in alphabet:
                flask.flash(f"Your name must be made up of letters in the alphabet.")
                return flask.render_template("index.html",form=form)
        for letterl in name[1]:
            if letterl not in alphabet:
                flask.flash(f"Your name must be made up of letters in the alphabet.")
                return flask.render_template("index.html",form=form)
        found_match=form.locate_user(name)
        if found_match:
            flask.flash(f"{name[0]} {name[1]}, you are already registered!")
        else:
            form.add_user(name)
            flask.flash(f"{name[0]} {name[1]}, you have just signed up!")
        return flask.redirect(flask.url_for('index',form=form))

    return flask.render_template("index.html",form=form)