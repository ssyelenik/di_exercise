import flask
from . import app,db
from . import models,forms

global matching_entry

@app.route("/", methods=['GET','POST'])
def index():
    global matching_entry
    matching_entry=""
    form = forms.SetSearch()
    if form.validate_on_submit():
        name="empty"
        phone_num="empty"
        try:
            name=flask.request.form['name']
            print(name)
            matching_entry=models.Person.query.filter_by(name=name).first()
            if not matching_entry==None:
                return flask.redirect(flask.url_for('display'))
            elif not name=='':
                flask.flash("Your search was not found in the phone book.")
                return flask.redirect(flask.url_for('index'))
        except:
            pass

        try:
            phone_num=flask.request.form['phone_num']
            print(phone_num)
            matching_entry=models.Person.query.filter_by(phone_num=phone_num).first()
            if not matching_entry==None:
                return flask.redirect(flask.url_for('display',matching_entry=matching_entry))
            elif not phone=='':
                flask.flash("Your search was not found in the phone book.")
                return flask.redirect(flask.url_for('index'))
        except:
            pass

        if phone_num=="" and name=="":
            print("here")
            flask.flash("You didn't enter a search parameter")
            return flask.redirect(flask.url_for('index'))

    return flask.render_template("index.html",form=form)

@app.route("/display", methods=['GET','POST'])
def display():
    global matching_entry
    print("got to display")
    form=forms.Display()
    return flask.render_template("display.html",matching_entry=matching_entry)

