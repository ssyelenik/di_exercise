import flask
from . import app

@app.route("/", methods=['GET','POST'])
def homepage():
    if flask.request.method=="POST":
        all_info=flask.request.form.to_dict()
        template_choice=flask.request.form['template_choice']
        url="home.bin/"+template_choice+".html"
        return flask.render_template(url,all_info=all_info)
    return flask.render_template("home.bin/enter_info.html")

@app.route('/<template_choice>')
def CV(all_info):
    print("template page",template_choice,"\n",all_info)
    return flask.render_template(flask.url_for("CV",template_choice=template_choice,all_info=all_info))