# This is a form for when users want to register or login into the site 

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User

class RegistrationForm(FlaskForm):

    first_name = StringField("First Name", 
                             validators=[DataRequired(), Length(min=2, max=20)])
    
    last_name = StringField("Last Name", 
                             validators=[DataRequired(), Length(min=2, max=20)])
    
    username = StringField("Username", 
                             validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("Register")

    def validate_first_name(self, first_name):
        user = User.query.filter_by(first_name = first_name.data).first()
        if user:
            raise ValidationError('Firstname already exist please choose a different one')
        
    def validate_last_name(self, last_name):
        user = User.query.filter_by(last_name = last_name.data).first()
        if user:
            raise ValidationError('Lastname already exist please choose a different one')
        
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username already exist please choose a different one')
        
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email already exist please choose a different one')

class LoginForm(FlaskForm):
     
    username = StringField("Username", 
                             validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    remember_user = BooleanField("Remember Me")

    submit = SubmitField("Login")
