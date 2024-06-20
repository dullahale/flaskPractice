# A file to hold our database modules

from flaskblog import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
# This function takes a user ID as an argument
def load_user(user_id):
    return User.query.get(int(user_id))

# Creating a table with columns and rows the contain user information 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default= "default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

# a method used to define the string representation of an object
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
# Creating a table for post database 
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# a method used to define the string representation of the class above
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"