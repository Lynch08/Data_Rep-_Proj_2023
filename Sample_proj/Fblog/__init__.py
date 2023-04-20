#Module Imports

from flask import Flask
#Import SQL ALalchemy
from flask_sqlalchemy import SQLAlchemy
#import classes from forms.py


app = Flask(__name__)

# set secret key to protect againest cookies and attacks
app.config['SECRET_KEY'] = '7e6224cc9ab38cbb4aa2e4c0312c036e'

#Instance of SQL DB in FLask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from Fblog import routes