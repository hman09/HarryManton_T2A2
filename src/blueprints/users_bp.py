# Need similar/identical imports as cli
from flask import Blueprint, request, jsonify
from setup import db
from models.user import User, UserSchema
from flask_jwt_extended import create_access_token, jwt_required
from blueprints.logs_bp import logs_bp
from sqlalchemy.exc import IntegrityError
from auth import authorise

users_bp = Blueprint('/', __name__) 

users_bp.register_blueprint(logs_bp)

# Home route (login)
@users_bp.route('/', methods=['POST'])
def login():
    user_info = UserSchema().load(request.json)
    stmt = db.select(User).where(User.email == user_info['email'])
    user = db.session.scalar(stmt)
    if user:
        token = create_access_token(identity=user.id)        
        return {'token': token, 'user': UserSchema(exclude=['password']).dump(user)}
    else:
        return {"error": "Invalid Email or Username"}

# Sign up route
@users_bp.route('/signup', methods=['POST'])
def signup():
    try:
        user_info = UserSchema().load(request.json)
        user = User(
            email=user_info['email'],
            username=user_info['username'],
            password=user_info['password']
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['is_admin']).dump(user)
    except IntegrityError:
        return {'Error' : 'Email or Username already in use.'}
        
# Make Root for finding 1 user
@users_bp.route('/<int:id>')
@jwt_required()
def single_user(id):
    authorise()
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['email','password','comments']).dump(user) #### ------------------- this may be an error
    else:
        return {'error' : 'User not found'}, 404
