import flask_wtf
import wtforms as wtf
import wtforms.validators as vald

class RegistrationForm(flask_wtf.FlaskForm):

    name     = wtf.StringField("Name", validators=[vald.DataRequired()])
    email    = wtf.StringField("Email", validators=[vald.DataRequired()])
    password = wtf.PasswordField("Password", validators=[vald.DataRequired()])
    confirm  = wtf.PasswordField("Confirm password", validators=[vald.EqualTo("password")])
    role     = wtf.SelectField("Role")

    submit   = wtf.SubmitField("Register")

class LoginForm(flask_wtf.FlaskForm):
    email    = wtf.StringField("Email", validators=[vald.DataRequired()])
    password = wtf.PasswordField("Password", validators=[vald.DataRequired()])

    submit   = wtf.SubmitField("Sign in")