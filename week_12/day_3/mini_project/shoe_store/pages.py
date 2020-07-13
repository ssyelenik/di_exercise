from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from pathlib import Path
import json

class confirm_order(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])

class employee_sign_in(FlaskForm):
    password = StringField('Password', validators=[DataRequired()])


