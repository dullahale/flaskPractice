from flask import Flask
from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__)

app.config['SECRET_KEY'] = "56de93dfdddc2a8d8d4d9e41e907c6d8"

# SQLAlchemy a flask extension that simplifies database integration 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

from flaskblog import routes