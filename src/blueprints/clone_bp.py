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



# # Create clone
# @clone_bp.route('/<int:id>') 
# @jwt_required()
# def create_clone(id):
#     log = Log.query.get(id)
#     if log:
#         find_max_id = db.session.query(Recipe.id).order_by(Recipe.id.desc()).first()
#         max_id = find_max_id[0]
#         print(find_max_id)
#         cloned_log = Log(
#             title = log.title,
#             recipe = log.recipe,
#             user_id = get_jwt_identity()
#         )
#         log.recipe.id = max_id+1
#         print(log.recipe.id)
#         db.session.add(cloned_log)
#         db.session.commit()
#         return LogSchema(only=['user', 'title', 'recipe']).dump(cloned_log), 201
#     else:
#         return {'error' : 'Log not found'}, 404


    

    
    
    
    
    
    # clone_info = LogSchema(exclude=['id']).load(request.json)
    # clone = Log(
    #     title = clone_info['title'],
    #     user_id = get_jwt_identity()
    # )
    # db.session.add(clone)
    # db.session.commit()
    # return LogSchema(exclude=['user','comments']).dump(clone), 201

    # Create comment

# @comments_bp.route('/<int:log_id>', methods=['POST']) 
# @jwt_required()
# def create_comment(log_id):
#     comment_info = CommentSchema().load(request.json)
#     comment = Comment(
#         message = comment_info['message'],
#         user_id = get_jwt_identity(),
#         log_id = log_id
#     )
#     db.session.add(comment)
#     db.session.commit()
    # return CommentSchema(only=['message']).dump(comment), 201