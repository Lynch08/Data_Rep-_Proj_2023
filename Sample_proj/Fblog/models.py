
from datetime import datetime
from Fblog import db, login_manager
#fask extension gives class to inherite from that adds these attributes and methods (is authenticated, is active, is annonomous, get_id)
from flask_login import UserMixin

#decorator
@login_manager.user_loader 
#function to fimd userby id
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref = 'author', lazy = True) #backref gets the user that created the post (1 to many relationship)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) # Foregin Key is refrencing the table and column names

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
