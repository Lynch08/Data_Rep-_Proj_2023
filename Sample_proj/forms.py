# form validation with Flask
# https://pythonspot.com/flask-web-forms/
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
# data required validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

# create registration form class
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)]) # requires data but limits charaters
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    # Create button to Submit data
    submit = SubmitField('Sign Up')


# create Login form class
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    # Create button to Submit data
    submit = SubmitField('Login')



