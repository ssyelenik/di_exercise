import flask
from . import app
import flask_login
from . import login_mngr,models
from . import db


@app.route("/", methods=['GET','POST'])
def home():
    return flask.render_template("home.html")


@app.route("/add", methods=['GET','POST'])
def add():
    if flask.request.method=="POST":
        user = models.User.query.all()
        for u in user:
            if u.email==flask.request.form["email"] or u.password==flask.request.form["password"]:
                flask.flash("Your email or password has already been taken. Please try again.", category="error")
                return flask.redirect(flask.url_for("home"))
        email=flask.request.form['email']
        password=flask.request.form['password']
        tp=flask.request.form['type']
        new_user=models.User(email=email,password=password,type=tp)
        db.session.add(new_user)
        db.session.commit()
        flask.flash('New user with user id {} has been added to the database.'.format(new_user.id))
        print(tp)
        if tp=="Teacher":
            print("Teacher here")
            return flask.redirect(flask.url_for("teacher_view"))
        else:
            print("student here")
            return flask.redirect(flask.url_for("student_view"))
    return flask.render_template("add.html")

@app.route("/login", methods=['POST', "GET"])
def login():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(flask.url_for('home'))
    if flask.request.method=="POST":
        user=models.User.query.filter_by(email=flask.request.form['email']).first()
        if user is None or not user.password==flask.request.form['password']:
            flask.flash("Invalid username or password")
            return flask.redirect(flask.url_for('login'))
        flask_login.login_user(user)
        flask.flash(f'User with user id {user.id} is logged in.')
        if user.type=="Teacher":
            return flask.redirect(flask.url_for("teacher_view"))
        else:
            return flask.redirect(flask.url_for("student_view"))
    return flask.render_template('login.html')

    # user = models.User.query.filter_by(email=flask.request.form['email']).first()
    # if "login" in flask.request.form:
    #     if user:
    #         if user.password==flask.request.form['password']:
    #             db.session['user']=user.id
    #             if user.type=="Teacher":
    #                 return flask.render_template("teacher_view.html")
    #             if user.type=="Student":
    #                 return flask.render_template("student_view.html")
    #         else:
    #             flask.flash("password incorrect")
    #             return flask.redirect(flask.url_for("home"))
    #     else:
    #         flask.flash("user doesn't exist")
    #         return flask.redirect(flask.url_for('home'))
    # else:
    #     if user:
    #         if user.email==flask.request.form['email']:
    #             flask.flash("Email is take. Please use another")
    #     else:
    #         new_user=models.User(email=flask.request.form['email'], password=flask.request.form['password'],
    #                               type=flask.request.form['type'])
    #         db.session.add(new_user)
    #         db.session.commit()
    #         if flask.request.form['type']=='Teacher':
    #             return flask.redirect(flask.url_for('teacher_view'))
    #         else:
    #             return flask.redirect(flask.url_for('student_view'))
    # return flask.redirect(flask.url_for('home'))

@app.route("/teacher_view")
def teacher_view():
    return flask.render_template("teacher_view.html")

@app.route("/student_view")
def student_view():
    return flask.render_template("student_view.html")

@app.route("/signout")
def logout():
    id=flask_login.current_user.id
    flask.flash(f'Goodbye, user with id {id}.')
    flask_login.logout_user()
    return flask.redirect(flask.url_for('home'))
