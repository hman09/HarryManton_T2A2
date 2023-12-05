# Need similar/identical imports as cli
from flask import Blueprint
from setup import db
from models.user import User

# Define Blueprint and config in app
users_bp = Blueprint('/', __name__) # no url prefix becuase users will be my head page

# when user can sign in with POST, API will check if user is in db if not will prompt them to /sign up

# Home route
@users_bp.route('/', methods=['POST'])
def login():
 # Load the parse
 # Search that user is in DB
 # If statment - user is valid, return "logged in" and give JWT
 # Else prompt them to sign up page. (will check if its possible to move the route to a signup page).


# Will need Error handling now.