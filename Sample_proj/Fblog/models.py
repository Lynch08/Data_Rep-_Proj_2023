from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from Fblog import db, login_manager, app
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

    #function to get reset token for login password
    def get_reset_token(self, expires_sec = 1800): #token expires in 30 mins
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8') #self is Object Oriented - this returns token from the dumps method that has a payload from the currentuser id

    #function to validate reset token for login password
    @staticmethod #tells python not to accept "self" as an argument - only token is accepted
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY']) #creates serializer
        try:
            user_id = s.loads(token)['user_id'] #tries to load token
        except:
            return None                         # an exception returns None
        return User.query.get(user_id)          # no exception return the user with the user_id

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
    
