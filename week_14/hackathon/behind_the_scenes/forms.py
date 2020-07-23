from flask_wtf import FlaskForm
import wtforms
import flask

class DatingSurvey(FlaskForm):
    first_name=wtforms.StringField("First Name")
    last_name=wtforms.StringField("Last Name")
    age_group=wtforms.SelectField("Age Group",choices=[("A","18-25"),("B","26-32"),("C","33-40"),("D","41-55"),("E","55-65"),("F","65-80")])

    status=wtforms.SelectField("Marriage Status",choices=[('NM', 'Never Married'), ('D', 'Divorced'), ('W', 'Widowed')])
    gender=wtforms.SelectField("Gender",choices=[('M', 'Male'), ('F', 'Female')])
    phone=wtforms.StringField("Phone Number")
    email=wtforms.StringField("Email")

    city=wtforms.StringField("City")
    state=wtforms.SelectField("State",choices=[(None,"None"),('Alabama','Alabama'),('Alaska','Alaska'),('Arizona','Arizona'),('Arkansas','Arkansas'),('California','California'),('Colorado','Colorado'),('Connecticut','Connecticut'),('Delaware','Delaware'),('Florida','Florida'),('Georgia','Georgia'),('Hawaii','Hawaii'),('Idaho','Idaho'),('Illinois','Illinois'),('Indiana','Indiana'),('Iowa','Iowa'),('Kansas','Kansas'),('Kentucky','Kentucky'),('Louisiana','Louisiana'),('Maine','Maine'),('Maryland','Maryland'),('Massachusetts','Massachusetts'),('Michigan','Michigan'),('Minnesota','Minnesota'),('Mississippi','Mississippi'),('Missouri','Missouri'),('Montana','Montana'),('Nebraska','Nebraska'),('Nevada','Nevada'),('New Hampshire','New Hampshire'),('New Jersey','New Jersey'),('New Mexico','New Mexico'),('New York','New York'),('North Carolina','North Carolina'),('North Dakota','North Dakota'),('Ohio','Ohio'),('Oklahoma','Oklahoma'),('Oregon','Oregon'),('Pennsylvania','Pennsylvania'),('Rhode Island','Rhode Island'),('South Carolina','South Carolina'),('South Dakota','South Dakota'),('Tennessee','Tennessee'),('Texas','Texas'),('Utah','Utah'),('Vermont','Vermont'),('Virginia','Virginia'),('Washington','Washington'),('West Virginia','West Virginia'),('Wisconsin','Wisconsin'),('Wyoming','Wyoming')])
    country=wtforms.SelectField("Country",choices=[('USA', 'USA'), ('France', 'France'), ('Israel', 'Israel'),('Canada', 'Canada')])
    hobbies=wtforms.SelectField("Hobbies",choices=[('Reading', 'Reading'), ('Exercising', 'Exercising'), ('Painting', 'Painting'),('Playing a musical instrument', 'Playing a musical instrument'),('Hiking', 'Hiking'),('Dining', 'Dining'),('Socializing', 'Socializing')])
    profession=wtforms.SelectField("Profession",choices=[('Doctor', 'Doctor'), ('Lawyer', 'Lawyer'), ('Chef', 'Chef'),('Beautician', 'Beautician'),('Scientist', 'Scientist'),('Engineer', 'Engineer'),('Psychologist', 'Psychologist'),('Coach', 'Coach'),('Driver', 'Driver'),('Teacher', 'Teacher'),('Salesperson', 'Salesperson')])
    personality=wtforms.SelectField("Personality",choices=[('Kind', 'Kind'), ('Energetic', 'Energetic'), ('Laid Back', 'Laid Back'),('Intellectual', 'Intellectual')])
    in_extrovert=wtforms.SelectField("Are you introverted or extroverted?",choices=[('Introverted', 'Introverted'), ('Extroverted', 'Extroverted')])

    image= wtforms.StringField('A picture of you')
    personal_comment=wtforms.TextAreaField("Personal Comment")

    submit=wtforms.SubmitField("Save New Todo")