from flask import Blueprint, request, jsonify
from setup import db
from models.comment import Comment, CommentSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from auth import authorise

comments_bp = Blueprint('/', __name__, url_prefix='/comments')

# Function TBD for change
def your_comments():
    user_id = get_jwt_identity()
    comments = db.session.query(Comment).filter_by(user_id=user_id).all()
    their_comments = CommentSchema(exclude=['user','logs','user_id'], many=True).dump(comments)
    return jsonify(their_comments)
    

# View your comments
@comments_bp.route('/')
@jwt_required()
def my_comments():
    return your_comments()

# Get logs comments
@comments_bp.route('<int:log_id>')
@jwt_required()
def log_comments(log_id):
    comments = db.session.query(Comment).filter_by(log_id=log_id).all()
    log_comments = CommentSchema(exclude=['logs', 'log_id', 'user_id'], many=True).dump(comments)
    return jsonify(log_comments)


# Get users comments, admin only
@comments_bp.route('/user<int:user_id>')
@jwt_required()
def user_comments(user_id):
    comments = db.session.query(Comment).filter_by(user_id=user_id).all()
    if comments:
        authorise()
        users_comments = CommentSchema(exclude=['user','logs','user_id'], many=True).dump(comments)
        return jsonify(users_comments)
    
    else:
        return {'error' : 'User not found'}, 404

#CRUD

# Create comment
@comments_bp.route('/<int:log_id>', methods=['POST']) 
@jwt_required()
def create_comment(log_id):
    comment_info = CommentSchema().load(request.json)
    comment = Comment(
        message = comment_info['message'],
        user_id = get_jwt_identity(),
        log_id = log_id
    )
    db.session.add(comment)
    db.session.commit()
    return CommentSchema(only=['message','id']).dump(comment), 201


# Update comment
@comments_bp.route('/edit/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_comment(id):
    comment_info = CommentSchema(exclude=['id']).load(request.json)
    stmt = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    if comment:
        authorise(comment.user_id)
        comment.message = comment_info.get('message', comment.message)
        db.session.commit()
        return CommentSchema(only=['message']).dump(comment), 200
    else:
        return {'error' : 'Comment not found'}, 404
    
# Delete comment
@comments_bp.route("delete/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_comment(id):
    stmt = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    if comment:
        authorise(comment.user_id)
        db.session.delete(comment)
        db.session.commit()
        return your_comments(), 200
    else:
        return {'error' : 'Comment not found'}, 404
