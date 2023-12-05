# Import mods to setup flask architype
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from os import environ

# Create app/ link app to db/ set JWT secret key/ Link .flaskenv to restirct info
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('SQLALCHEMY_DATABASE_URI')  # database connection string. it follows the following conventions. add in from time/10.58

app.config["JWT_SECRET_KEY"] = environ.get('JWT_SECRET_KEY')

# connect to app; Marshmellow for Schema/ SQLAlchemy for ORM/ Bcrypt for hashing/ JWT for authentication

ma = Marshmallow(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)