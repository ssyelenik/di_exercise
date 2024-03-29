import os
import flask
import flask_sqlalchemy
import flask_migrate

app=flask.Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(basedir,"app.db")
db=flask_sqlalchemy.SQLAlchemy(app)
migrate=flask_migrate.Migrate(app,db)
app.config['SECRET_KEY']="tryingthisoutforthefirsttime"
from . import views,models
