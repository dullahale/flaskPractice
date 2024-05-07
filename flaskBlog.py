from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = "56de93dfdddc2a8d8d4d9e41e907c6d8"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

# Creating a table with columns and rows the contain user information 
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
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
   

posts = [
    {
        'author': 'Dullah Ale',
        'title': 'First Blog Post',
        'content': 'First post content',
        'date_posted': 'April 22, 2024',
    },

     {
        'author': 'Victor Towobawa',
        'title': 'Second Blog Post',
        'content': 'Second post content',
        'date_posted': 'April 23, 2024',
    },

    {
        'author': 'Osama Abdullah',
        'title': 'Third Blog Post',
        'content': 'Third post content',
        'date_posted': 'April 26, 2024',
    },

    {
        'author': 'Osaze Dieseal',
        'title': 'Fourth Blog Post',
        'content': 'Fourth post content',
        'date_posted': 'April 30, 2024',
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("Form validation successful!")  # Add this for debugging
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    else:
        # If form validation fails, print out the validation errors to identify the issue
        print(form.errors)
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "user" and form.email.data == "user@blog.com" and form.password.data == "password":
            flash("You have logged in sucessfully", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username, email, or password. Please try again.", 'danger')
    return render_template("login.html", title="Login", form=form)



if __name__ == '__main__':
    app.run(debug=True)