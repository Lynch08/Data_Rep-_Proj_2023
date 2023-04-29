# form validation with Flask
# https://pythonspot.com/flask-web-forms/
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed # change profile pic
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
# data required validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# import from flskblog
from Fblog.models import User

# create registration form class
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)]) # requires data but limits charaters
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    # Create button to Submit data
    submit = SubmitField('Sign Up')

    #Function to validate username to avoid user createing duplicates
    def validate_username(self, username):
        user  = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That Username Already Exists - Please Choose again')

    #Function to validate username to avoid user createing duplicates
    def validate_email(self, email):
        user  = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That Email Already Exists - Please Choose again')

# create Login form class
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    # Create button to Submit data
    submit = SubmitField('Login')




class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)]) # requires data but limits charaters
    email = StringField("Email", validators=[DataRequired(),Email()])
    #for profile pic
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    # Create button to Submit data
    submit = SubmitField('Update')
    #Function to validate username to avoid user createing duplicates
    def validate_username(self, username):
        if username.data != current_user.username:
            user  = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That Username Already Exists - Please Choose again')

    #Function to validate username to avoid user createing duplicates
    def validate_email(self, email):
        if email.data != current_user.email:
            user  = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That Email Already Exists - Please Choose again')


class PostForm(FlaskForm):
    title = StringField('Title', validators =[DataRequired()] )
    content = TextAreaField('Content',  validators =[DataRequired()])
    submit = SubmitField('Post')


