from flask import Blueprint, request
from setup import db, bcrypt
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
    if user and bcrypt.check_password_hash(user.password, user_info['password']):
        token = create_access_token(identity=user.id)        
        return {'token': token, 'user': UserSchema(only=['username', 'id']).dump(user)}
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
            password=bcrypt.generate_password_hash(user_info["password"]).decode("utf8")
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema(only=['id','username','email']).dump(user)
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
        return UserSchema(exclude=['email','password']).dump(user)
    else:
        return {'error' : 'User not found'}, 404
