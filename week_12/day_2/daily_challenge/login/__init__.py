import flask
app=flask.Flask(__name__)
from . import views

app.config["SECRET_KEY"]="adkfjqwetnewmroviapkaeth"