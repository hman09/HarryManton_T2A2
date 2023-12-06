# Copy user_bp mods 
from flask import Blueprint, request, jsonify
from setup import db
from models.log import Log, LogSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

# Setup blueprint here and in app.py
# Set User as a parent route and require a user_id prefix
logs_bp = Blueprint('/', __name__, url_prefix='/logs')

# View your logs
@logs_bp.route('/')
@jwt_required()
def log_view():
    user_id = get_jwt_identity()
    logs = db.session.query(Log).filter_by(user_id=user_id).all()
    your_logs = LogSchema(many=True).dump(logs)
    return jsonify(your_logs)



# Get selected users log
@logs_bp.route('/<int:user_id>')
# Once working add @jwt_required() to force login
# Just noticed potential issue since users_bp has a route with just the user_id, will continue to explore results
def single_user(user_id):
    logs = db.session.query(Log).filter_by(user_id=user_id).all()
    print(logs)
    if logs:
        # had issue that mutliple logs were trying to be returned, made it only one log now works
        # Therefore just need to correct code below to fix
        # Fixed by using db.session.query so could iterate output
        users_logs = LogSchema(many=True).dump(logs)
        return jsonify(users_logs)
    
    else:
        return {'error' : 'User not found'}, 404