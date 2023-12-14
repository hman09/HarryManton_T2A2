from flask import Blueprint, request, jsonify
from setup import db
from models.log import Log, LogSchema
from models.recipe import Recipe
from flask_jwt_extended import jwt_required, get_jwt_identity

clone_bp = Blueprint('/clone', __name__, url_prefix='/clone')



# Create clone
@clone_bp.route('/<int:id>') 
@jwt_required()
def create_clone(id):
    log = Log.query.get(id)
    if log:
        cloned_log = Log(
            title = log.title,
            user_id = get_jwt_identity()
        )
        db.session.add(cloned_log)
        db.session.commit()

        for original_recipe in log.recipe:
            cloned_log_recipe = Recipe(
                flour_types = original_recipe.flour_types,
                flour_g = original_recipe.flour_g,
                water_g = original_recipe.water_g,
                starter_type = original_recipe.starter_type,
                starter_g = original_recipe.starter_g,
                bulk_fermentation_min = original_recipe.bulk_fermentation_min,
                knead = original_recipe.knead,
                log_id = cloned_log.id
            )
            db.session.add(cloned_log_recipe)
        db.session.commit()

        return LogSchema(only=['user', 'title', 'recipe']).dump(cloned_log), 201
    else:
        return {'error' : 'Log not found'}, 404
    
# @clone_bp.route('/get<int:id>') 
# @jwt_required()
# def clone(id):
#     log = Log.query.get(id)
#     if log:
#         cloned_log = Log(
#             title=log.title,
#             user_id=get_jwt_identity()
#         )
#         db.session.add(cloned_log)
#         db.session.commit()

#         for original_recipe in log.recipe:
#             cloned_log_recipe = Recipe(
#                 log_id=log.id
#             )
            
#             for field in original_recipe.__table__.columns:
#                 field_name = field.name
#                 if field_name != ('id' or 'log_id') and hasattr(cloned_log_recipe, field_name):
#                     setattr(cloned_log_recipe, field_name, getattr(original_recipe, field_name))
            
#             db.session.add(cloned_log_recipe)
#         db.session.commit()
        
#         return LogSchema(only=['user', 'title', 'recipe']).dump(cloned_log), 201
#     else:
#         return {'error': 'Log not found'}, 404
