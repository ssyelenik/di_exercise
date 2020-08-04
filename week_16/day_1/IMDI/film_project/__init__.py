import flask
import os
import flask_sqlalchemy
import flask_migrate
import flask_login
from .utils import ListConverter


app=flask.Flask(__name__)
app.url_map.converters['list'] = ListConverter
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(basedir,"app.db")
db=flask_sqlalchemy.SQLAlchemy(app)
migrate=flask_migrate.Migrate(app,db)
app.config['SECRET_KEY']="qpwlekvheksltuiw"
login_mgr=flask_login.LoginManager(app)
from . import views,models