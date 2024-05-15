from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
from forms import RegistrationForm, LoginForm
from models import User, Post


app = Flask(__name__)

app.config['SECRET_KEY'] = "56de93dfdddc2a8d8d4d9e41e907c6d8"
# SQLAlchemy a flask extension that simplifies database integration 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)


   

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