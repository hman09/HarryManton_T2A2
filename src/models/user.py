from setup import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)

    logs = db.relationship('Log', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')

class UserSchema(ma.Schema):
    logs = fields.Nested('LogSchema', exclude=['user'], many=True)
    comments = fields.Nested('CommentSchema', only=['message'], many=True)
    class Meta:
        fields = ('id', 'email', 'username', 'password', 'is_admin', 'logs', 'comments')