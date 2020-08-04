from flask_wtf import FlaskForm
import wtforms
from datetime import datetime

class AddFilm(FlaskForm):
    title=wtforms.StringField("Title",[wtforms.validators.DataRequired()])
    release_date=wtforms.StringField("Release Date", default=str(datetime.today().strftime('%Y-%m-%d')), validators=[wtforms.validators.DataRequired(message="You need to enter the release date")],)
    country_of_origin=wtforms.SelectField("Created in")
    available_in_countries=wtforms.SelectMultipleField("Available in")
    director=wtforms.SelectMultipleField("Director(s)")
    category=wtforms.SelectMultipleField("Category")
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