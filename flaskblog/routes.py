from flask import render_template, url_for, flash, redirect
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user


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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name = form.first_name.data, last_name = form.last_name.data, 
                    username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been successfully created! You are now able to login', 'success')
        return redirect(url_for('login'))
    else:
        # If form validation fails, print out the validation errors to identify the issue
        print(form.errors)
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_user.data)
            return redirect(url_for('home'))
        else:
            flash("Invalid username, email, or password. Please try again.", 'danger')
    return render_template("login.html", title="Login", form=form)
