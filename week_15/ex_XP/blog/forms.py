from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
import wtforms
from flask_uploads import UploadSet, IMAGES
import email_validator
import flask
from . import photos

class AddUser(FlaskForm):
    username = wtforms.StringField("User Name",[wtforms.validators.DataRequired()])
    email = wtforms.StringField("Email Address",[wtforms.validators.DataRequired(),wtforms.validators.Email()])
    password = wtforms.PasswordField("Password",[wtforms.validators.DataRequired()])
    confirm_password=wtforms.PasswordField("Confirm Password",[wtforms.validators.DataRequired(),wtforms.validators.EqualTo('password',message="Must match password")])
    submit=wtforms.SubmitField("Save New User")

class Login(FlaskForm):
    username = wtforms.StringField("User Name",[wtforms.validators.DataRequired()])
    password = wtforms.PasswordField("Password",[wtforms.validators.DataRequired()])
    submit=wtforms.SubmitField("Login")


class PostBlog(FlaskForm):
    headline= wtforms.StringField("Headline",[wtforms.validators.DataRequired()])
    body=wtforms.TextAreaField("Blog",[wtforms.validators.DataRequired()])
    photo = FileField("Picture",validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
    tags=wtforms.SelectMultipleField("Tags")
    new_tags=wtforms.StringField("Additional Tags")
    submit=wtforms.SubmitField("Save New Blog")



