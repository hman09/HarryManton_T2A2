# Need similar/identical imports as cli
from flask import Blueprint, request, redirect
from setup import db
from models.user import User, UserSchema
from flask_jwt_extended import create_access_token, jwt_required
from blueprints.logs_bp import logs_bp

# Define Blueprint and config in app
users_bp = Blueprint('/', __name__) # no url prefix becuase users will be my head page

users_bp.register_blueprint(logs_bp)

# Home route
@users_bp.route('/', methods=['POST'])
def login():
    # Load the parse
    user_info = UserSchema().load(request.json)
    # Search that user is in DB, use email to identify the user
    stmt = db.select(User).where(User.email == user_info['email'])
    user = db.session.scalar(stmt)
    # If statment - user is valid, return "logged in" and give JWT
    if user:
        token = create_access_token(identity=user.id)        
        return {'token': token, 'user': UserSchema().dump(user)}
    # Else prompt them to sign up page. (will check if its possible to move the route to a signup page)
    # found redirect in flask will use elif to redirect to the signup page if account cant be found
    # elif User.email != user_info['email']:
    #     print('done')
    #     return redirect('signup', )
    # Dropping idea will remove after a push for documentation
    else:
        return {"error": "Invalid Email or Username"}

# Sign up route
@users_bp.route('/signup', methods=['POST'])
def signup():
    # Load parse
    user_info = UserSchema().load(request.json)
    # Put info into UserSchema
    user = User(
        email=user_info['email'],
        username=user_info['username']
    )
    # Add and commit
    db.session.add(user)
    db.session.commit()
    # Return them the user details
    return UserSchema().dump(user)
    
# Make Root for finding 1 user
@users_bp.route('/<int:id>')
@jwt_required()
def single_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['email']).dump(user)
    else:
        return {'error' : 'User not found'}, 404
