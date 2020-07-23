import flask
import flask_migrate
import flask_sqlalchemy
import os

app=flask.Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(basedir,"app.db")
db=flask_sqlalchemy.SQLAlchemy(app)
migrate=flask_migrate.Migrate(app,db)
app.config['SECRET_KEY']="thisisahachathoncalledbehindthescenes"

from . import views,models,forms


