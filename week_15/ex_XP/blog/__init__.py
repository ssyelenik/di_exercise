import flask
import os
import flask_sqlalchemy
import flask_migrate
import flask_login
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

app=flask.Flask(__name__)
basedir=os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(basedir,"app.db")
db=flask_sqlalchemy.SQLAlchemy(app)
migrate=flask_migrate.Migrate(app,db)
app.config['SECRET_KEY']="afksldewuqopiu"
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'uploads')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)
login_mngr=flask_login.LoginManager(app)
from . import views, models

