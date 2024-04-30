# This is a form for when users want to register or login into the site 

from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(Flaskform):

    first_name = StringField("First Name", 
                             validators=[DataRequired(), Length(min=2, max=20)])
    
    last_name = StringField("Last Name", 
                             validators=[DataRequired(), Length(min=2, max=20)])
    
    username = StringField("Username", 
                             validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo("passsword")])

    submit = SubmitField("Register")

class LoginForm(Flaskform):
     
    username = StringField("Username", 
                             validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo("passsword")])

    submit = SubmitField("Register")
