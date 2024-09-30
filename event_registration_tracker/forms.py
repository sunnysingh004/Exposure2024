from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateTimeField('Date and Time', validators=[DataRequired()])
    location = StringField('Location')
    description = TextAreaField('Description')
    category = SelectField('Category', choices=[('Workshop', 'Workshop'), ('Seminar', 'Seminar'), ('Social', 'Social')])
    submit = SubmitField('Create Event')
