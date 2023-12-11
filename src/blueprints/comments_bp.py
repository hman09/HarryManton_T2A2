# copy paste comments_bp and edit
# make child of log (register there)
# ran print(app.url_map) to review current routing path and plan optimal comment route
# below after from print out
    #  <Rule '/logs/comments/' (OPTIONS, HEAD, GET) -> /././.comment_view>,
    #  <Rule '/logs/comments/<user_id>' (OPTIONS, HEAD, GET) -> /././.single_user>,
    #  <Rule '/logs/comments/' (OPTIONS, POST) -> /././.create_comment>,
    #  <Rule '/logs/comments/edit/<id>' (PUT, OPTIONS, PATCH) -> /././.update_comment>,
    #  <Rule '/logs/comments/delete/<id>' (OPTIONS, DELETE) -> /././.delete_comment>])
# adding log int prefix before 'comment' should create logical flow
# will comment out all expect CREATE to test

from flask import Blueprint, request, jsonify
from setup import db
from models.comment import Comment, CommentSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from auth import authorise

comments_bp = Blueprint('/', __name__, url_prefix='<int:log_id>/comments')

@comments_bp.route('/', methods=['POST']) 
#@jwt_required()
def create_comment():
    comment_info = CommentSchema().load(request.json)
    comment = Comment(
        comment = comment_info['comment'],
        user_id = get_jwt_identity()
    )
    db.session.add(comment)
    db.session.commit()
    return CommentSchema(only=['comment']).dump(comment), 201

# # Function for return all users comments, include for read and delete. Create and edit will be clearer if only 1 output is resolved. 
# def users_comments():
#     user_id = get_jwt_identity()
#     comments = db.session.query(Comment).filter_by(user_id=user_id).all()
#     their_comments = CommentSchema(exclude=['user'], many=True).dump(comments)
#     return jsonify(their_comments)

# # View your comments
# @comments_bp.route('/')
# @jwt_required()
# def comment_view():
#     return users_comments()




# # Get selected users comment
# @comments_bp.route('/<int:user_id>')
# # @jwt_required()
# def single_user(user_id):
#     comments = db.session.query(Comment).filter_by(user_id=user_id).all()
#     if comments:
#         users_comments = CommentSchema(exclude=['user'], many=True).dump(comments)
#         return jsonify(users_comments)
    
#     else:
#         return {'error' : 'User not found'}, 404

#CRUD

# Create comment

#----------------------------------------------------------------

# Read already done above

# # Update comment
# @comments_bp.route('/edit/<int:id>', methods=['PUT', 'PATCH'])
# @jwt_required()
# def update_comment(id):
#     comment_info = CommentSchema(exclude=['id']).load(request.json)
#     stmt = db.select(Comment).filter_by(id=id)
#     comment = db.session.scalar(stmt)
#     if comment:
#         authorise(comment.user_id)
#         comment.title = comment_info.get('title', comment.title)
#         db.session.commit()
#         return CommentSchema(exclude=['user']).dump(comment), 200
#     else:
#         return {'error' : 'Comment not found'}, 404
    
# # Delete comment
# @comments_bp.route("delete/<int:id>", methods=["DELETE"])
# @jwt_required()
# def delete_comment(id):
#     stmt = db.select(Comment).filter_by(id=id)
#     comment = db.session.scalar(stmt)
#     if comment:
#         authorise(comment.user_id)
#         db.session.delete(comment)
#         db.session.commit()
#         return users_comments(), 200
#     else:
#         return {'error' : 'Comment not found'}, 404
