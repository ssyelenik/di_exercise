from flask_wtf import FlaskForm
import wtforms
from datetime import datetime
from flask_wtf.file import FileField,FileAllowed,FileRequired
from flask_uploads import UploadSet, IMAGES

photos=UploadSet('photos',IMAGES)

class AddFilm(FlaskForm):
    title=wtforms.StringField("Title",[wtforms.validators.DataRequired()])
    release_date=wtforms.StringField("Release Date", default=str(datetime.today().strftime('%Y-%m-%d')), validators=[wtforms.validators.DataRequired(message="You need to enter the release date")],)
    country_of_origin=wtforms.SelectField("Created in")
    available_in_countries=wtforms.SelectMultipleField("Available in")
    director=wtforms.SelectMultipleField("Director(s)")
    category=wtforms.SelectMultipleField("Category")
    photo = FileField("Picture",validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
    explanation=wtforms.StringField("Photo Explanation")
    submit=wtforms.SubmitField("Add Film")

class ModifyFilm(FlaskForm):
    title=wtforms.StringField("Title",[wtforms.validators.DataRequired()])
    release_date=wtforms.StringField("Release Date", validators=[wtforms.validators.DataRequired(message="You need to enter the release date")],)
    country_of_origin=wtforms.SelectField("Created in")
    category=wtforms.SelectMultipleField("Category")
    submit=wtforms.SubmitField("Modify Film")

class AddDirector(FlaskForm):
    first_name=wtforms.StringField("First Name",[wtforms.validators.DataRequired()])
    last_name=wtforms.StringField("Last Name",[wtforms.validators.DataRequired()])
    film=wtforms.SelectField("Film")
    submit=wtforms.SubmitField("Add Director")

class ModifyDirector(FlaskForm):
    first_name=wtforms.StringField("First Name",[wtforms.validators.DataRequired()])
    last_name=wtforms.StringField("Last Name",[wtforms.validators.DataRequired()])

    submit=wtforms.SubmitField("Modify Director")

class DeleteFilm(FlaskForm):
    title=wtforms.SelectField("Title")
    submit=wtforms.SubmitField("Delete Film")

class DeleteDirector(FlaskForm):
    director=wtforms.SelectField("Director")
    submit=wtforms.SubmitField("Delete Director")

class FilmRating(FlaskForm):
    num=wtforms.SelectField("Number Rating")
    comment=wtforms.StringField("Comment")
    submit=wtforms.SubmitField("Submit Rating")