#create the application object as an instance of class Flask imported from the flask package
from flask import Flask
#import the Config class that has the configurations for the app
from config import Config
#importing various packages
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#predefined variable set to the name of the module in which it is used
app = Flask(__name__)
#instruct flask to read from the config file
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
#instructing flask login the view function that handles login
login = LoginManager(app)
login.login_view = 'login'
from app import routes, models