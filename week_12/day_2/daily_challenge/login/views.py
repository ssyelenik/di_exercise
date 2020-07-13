from . import forms
import flask
from . import app
from pathlib import Path
import json

@app.route("/", methods=['GET','POST'])
def index():
    form = forms.MyForm()
    if form.validate_on_submit():
        name=[flask.request.form['first_name'],flask.request.form['last_name'],flask.request.form['favorite_color']]
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
        if not found_match=="new_user":
            if found_match["status"]=="admin":
                flask.flash(f"{name[0]} {name[1]}, you are an admin user!")
                print("here")
                print(found_match["status"])

                data_folder=Path("C:/BootCamp/di_exercise/week_12/day_2/daily_challenge/login/")
                file_to_open=data_folder / "user.json"
                with open(file_to_open,"r") as users:
                    users=json.load(users)
                return flask.render_template('admin_form.html',users=users)
            else:
                flask.flash(f"{name[0]} {name[1]}, you are already registered!")
        else:
            form.add_user(name)
            flask.flash(f"{name[0]} {name[1]}, you have just signed up!")
        return flask.redirect(flask.url_for('index',form=form))
    return flask.render_template("index.html",form=form)

@app.route("/admin", methods=['GET','POST'])
def admin_form(users):

    # users=utilities.get_users()
    # form=admin_form(users)
    # if form.vaildate_on_submit():
    #
    #     user_id=form.user_id.data
    #     first_name=form.first_name.data
    #     last_name=form.last_name.data
    #     favorite_color=form.favorite_color.data

    return flask.render_template("admin_form.html",users=users)


@app.route("/view_user", methods=['GET','POST'])
def view_user():
    user={"id":flask.request.form['id'],"first_name":flask.request.form['first_name'],"last_name":flask.request.form['last_name'],"favorite_color":flask.request.form['favorite_color']}

    try:
        button=flask.request.form['submit_changes']
        updated_user={"id":flask.request.form['id'],"first_name":flask.request.form['first_name'],"last_name":flask.request.form['last_name'],"favorite_color":flask.request.form['favorite_color']}
        data_folder=Path("C:/BootCamp/di_exercise/week_12/day_2/daily_challenge/login/")
        file_to_open=data_folder / "user.json"
        with open(file_to_open,"r") as f:
            users=json.load(f)
        print(users)
        for i in range(len(users)):
            print(updated_user['id'])
            print(users[i]['id'])
            if int(users[i]['id'])==int(updated_user['id']):
                print("match found")
                users[i]['first_name']=updated_user['first_name']
                users[i]['last_name']=updated_user['last_name']
                users[i]['favorite_color']=updated_user['favorite_color']
                print(users[i])
                break
        with open(file_to_open,"w") as f:
            json.dump(users,f,indent=4)

        flask.flash(f"Updated user {updated_user['first_name']} {updated_user['last_name']}")
        return flask.render_template('admin_form.html',users=users)
    except:
        pass
    return flask.render_template("view_user.html",user=user)