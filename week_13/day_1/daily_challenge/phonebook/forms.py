
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class SetSearch(FlaskForm):
    name = StringField('Name:')
    phone_num = StringField('Phone Number:')
    submit = SubmitField('Submit')

class Display(FlaskForm):
    id = StringField('ID:')
    phone_num = StringField('Phone Number:')
    name = StringField('Name:')
    email=StringField('Email:')
    address=StringField('Address:')
    submit = SubmitField('Submit')
