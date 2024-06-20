from flaskblog import app, db
from flaskblog.models import User

with app.app_context():
    users = User.query.all()
    for user in users:
        print(f"ID: {user.id}, First Name:{user.first_name}," 
              f"Last Name: {user.last_name}, Username: {user.username},"
              f" Email: {user.email}, Password: {user.password}")