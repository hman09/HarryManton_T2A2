from flask import Blueprint, request, jsonify
from setup import db
from models.log import Log, LogSchema
from models.recipe import Recipe
from models.comment import Comment
from flask_jwt_extended import jwt_required, get_jwt_identity
from auth import authorise
from blueprints.comments_bp import comments_bp
from blueprints.clone_bp import clone_bp


logs_bp = Blueprint('/', __name__, url_prefix='/logs')

logs_bp.register_blueprint(comments_bp)
logs_bp.register_blueprint(clone_bp)


# Function that may change to return all if Admin TBD
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
@jwt_required()
def single_user(user_id):
    logs = db.session.query(Log).filter_by(user_id=user_id).all()
    if logs:
        users_logs = LogSchema(exclude=['user', 'user_id'], many=True).dump(logs)
        return jsonify(users_logs)    
    else:
        return {'error' : 'User not found'}, 404

# View targeted log    
@logs_bp.route('/target/<int:id>')
@jwt_required()
def target_log(id):
    stmt = db.select(Log).filter_by(id=id)
    log = db.session.scalar(stmt)
    if log:
        return LogSchema(only=['comments','user','title', 'recipe']).dump(log)
    else:
        return {'error' : 'Log not found'}, 404

    
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
    for original_recipe in log_info['recipe']:
        log_recipe = Recipe(
            flour_types=original_recipe.get('flour_types', 'DefaultFlourType'),
            flour_g=original_recipe.get('flour_g', 0),  
            water_g=original_recipe.get('water_g', 0),  
            starter_type=original_recipe.get('starter_type', 'DefaultStarterType'),
            starter_g=original_recipe.get('starter_g', 0), 
            bulk_fermentation_min=original_recipe.get('bulk_fermentation_min', 0),
            knead=original_recipe.get('knead', 'DefaultKnead'),
            log_id=log.id
        )
    db.session.add(log_recipe)
    db.session.commit()
    return LogSchema(exclude=['user','comments']).dump(log), 201

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
        for original_recipe in log_info['recipe']:
            log_recipe = Recipe(
            flour_types=original_recipe.get('flour_types', 'DefaultFlourType'),
            flour_g=original_recipe.get('flour_g', 0),  
            water_g=original_recipe.get('water_g', 0),  
            starter_type=original_recipe.get('starter_type', 'DefaultStarterType'),
            starter_g=original_recipe.get('starter_g', 0), 
            bulk_fermentation_min=original_recipe.get('bulk_fermentation_min', 0),
            knead=original_recipe.get('knead', 'DefaultKnead'),
            log_id=log.id,
            id=id 
        )
        db.session.query(Recipe).filter_by(log_id=log.id).delete()
        db.session.add(log_recipe)
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
        db.session.query(Recipe).filter_by(log_id=log.id).delete()
        db.session.query(Comment).filter_by(log_id=log.id).delete()
        db.session.delete(log)
        db.session.commit()
        return user_logs(), 200
    else:
        return {'error' : 'Log not found'}, 404
