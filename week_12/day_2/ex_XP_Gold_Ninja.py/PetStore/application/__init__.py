import flask
app=flask.Flask(__name__)
from . import routes

app.config['SECRET_KEY']="adsklfjakjsafkldshdlqerwiuOvnakasdkjfjaeoriqupew"
