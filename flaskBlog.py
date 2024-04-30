from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "56de93dfdddc2a8d8d4d9e41e907c6d8"

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
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)



if __name__ == '__main__':
    app.run(debug=True)