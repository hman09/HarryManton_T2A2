from flask import Blueprint, request, jsonify
from setup import db
from models.log import Log, LogSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from auth import authorise
from blueprints.comments_bp import comments_bp

logs_bp = Blueprint('/', __name__, url_prefix='/logs')

logs_bp.register_blueprint(comments_bp)


# Function for return all users logs, include for read and delete. Create and edit will be clearer if only 1 output is resolved. 
def user_logs():
    user_id = get_jwt_identity()
    logs = db.session.query(Log).filter_by(user_id=user_id).all()
    their_logs = LogSchema(exclude=['user'], many=True).dump(logs)
    return jsonify(their_logs)

# View your logs
@logs_bp.route('/')
@jwt_required()
def log_view():
    return user_logs()

# Get selected users log
@logs_bp.route('/<int:user_id>')
# @jwt_required()
def single_user(user_id):
    logs = db.session.query(Log).filter_by(user_id=user_id).all()
    if logs:
        users_logs = LogSchema(exclude=['user', 'user_id'], many=True).dump(logs)
        return jsonify(users_logs)    
    else:
        return {'error' : 'User not found'}, 404

# View targeted log    
@logs_bp.route('/target/<int:id>')
#@jwt_required()
def target_log(id):
    stmt = db.select(Log).filter_by(id=id)
    log = db.session.scalar(stmt)
    if log:
        return LogSchema(exclude=['user_id']).dump(log)
    else:
        return {'error' : 'User not found'}, 404

    
#CRUD

# Create log
@logs_bp.route('/', methods=['POST']) 
@jwt_required()
def create_log():
    log_info = LogSchema(exclude=['id']).load(request.json)
    log = Log(
        title = log_info['title'],
        user_id = get_jwt_identity()
    )
    db.session.add(log)
    db.session.commit()
    return LogSchema(exclude=['user','comments']).dump(log), 201 ###-------------------------------- this may be an error

# Read already done above

# Update log
@logs_bp.route('/edit/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_log(id):
    log_info = LogSchema(exclude=['id']).load(request.json)
    stmt = db.select(Log).filter_by(id=id)
    log = db.session.scalar(stmt)
    if log:
        authorise(log.user_id)
        log.title = log_info.get('title', log.title)
        db.session.commit()
        return LogSchema(exclude=['user']).dump(log), 200
    else:
        return {'error' : 'Log not found'}, 404
    
# Delete log
@logs_bp.route("delete/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_log(id):
    stmt = db.select(Log).filter_by(id=id)
    log = db.session.scalar(stmt)
    if log:
        authorise(log.user_id)
        db.session.delete(log)
        db.session.commit()
        return user_logs(), 200
    else:
        return {'error' : 'Log not found'}, 404
