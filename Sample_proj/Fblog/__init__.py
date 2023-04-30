#Module Imports
import os

from flask import Flask
#Import SQL ALalchemy
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from flask_login import LoginManager

from flask_mail import Mail


app = Flask(__name__)

# set secret key to protect againest cookies and attacks
app.config['SECRET_KEY'] = '7e6224cc9ab38cbb4aa2e4c0312c036e'

#Instance of SQL DB in FLask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#Flask Bcrypt for Passwords
bcrypt = Bcrypt(app)

# login extension from flask
login_manager = LoginManager(app)

#this tells extension wher the loginview is located
login_manager.login_view = 'login' #login is the function name of the disered route - will redirect you to login page if you try to get to this page but are not logged in 

#
login_manager.login_message_category = 'info' # info is a bootstrap class


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME']= 'endalynch1987@gmail.com'
app.config['MAIL_PASSWORD'] = 'qsefbabjpwxxklbn'
mail = Mail(app)

from Fblog import routes