
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired


class SetSearch(FlaskForm):
    name = StringField('Name:')
    phone_num = StringField('Phone Number:')
    action = SelectField('Action:', choices=[('view_person', 'View Phone Book Entry'), ('add_nationality', 'Add a Nationality to a Person')])
    submit = SubmitField('Submit')

class Display(FlaskForm):
    id = StringField('ID:')
    phone_num = StringField('Phone Number:')
    name = StringField('Name:')
    email=StringField('Email:')
    address=StringField('Address:')
    submit = SubmitField('Submit')

class AddPerson(FlaskForm):
    id = StringField('ID:')
    phone_num = StringField('Phone Number:')
    name = StringField('Name:')
    email=StringField('Email:')
    address=StringField('Address:')
    nationality = SelectField('Nationality:', choices=[('American', 'American'), ('French', 'French'),('Israeli', 'Israeli')])
    submit = SubmitField('Submit')

