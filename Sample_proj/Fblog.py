#Module Imports
from flask import Flask, render_template, url_for, flash, redirect
#Import SQL ALalchemy
from flask_sqlalchemy import SQLAlchemy
#import classes from forms.py
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# set secret key to protect againest cookies and attacks
app.config['SECRET_KEY'] = '7e6224cc9ab38cbb4aa2e4c0312c036e'

#Instance of SQL DB in FLask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.string(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"USer"

# Dummy Data
posts = [
    {
        'author': "Enda Lynch",
        'title': "Blog post 1",
        "content": "First Post Content",
        "date_posted": "April 13th 2023"
    },
    {
        'author': "Colm Lynch",
        'title': "Blog post 2",
        "content": "Second Post Content",
        "date_posted": "April 14th 2023"
    }
]



#root page(Homepage)
@app.route("/") 
@app.route("/home") 
def home():
    return render_template('home.html', posts = posts) # posts variable within the template is equal to the dummy data

#About page
@app.route("/about") 
def about():
    return render_template('about.html', title = 'About')

#Register Page
@app.route("/register", methods = ['GET', 'POST']) 
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): #send flash message
        flash(f'Account Created For {form.username.data}!','success') # success is a bootstrap class
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form = form)

#login Page
@app.route("/login", methods = ['GET', 'POST']) 
def login():
    form = LoginForm()
    if form.validate_on_submit(): #send flash message
        if form.email.data == 'admin@blog.com' and form.password.data =='password':
            flash("You Have Been Looged in!!", 'success') # success is a bootstrap class
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful - Please Check Username and Password', 'danger') # danger is a bootstrap class
    return render_template('login.html', title='Login', form = form)






if __name__== '__main__':
    app.run(debug=True)
