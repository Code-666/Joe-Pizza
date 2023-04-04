from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bf0e2aa9df98d010ef8bd21642a31f18f834487c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ria.db'

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = "login"

from pizzaria import routes, models