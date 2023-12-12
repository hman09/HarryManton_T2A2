# Import db and schema
from setup import db, ma
from marshmallow import fields

# Make basic User class, just PK, email and username for now
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)

    logs = db.relationship('Log', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')

# Use above for marshmallow
class UserSchema(ma.Schema):
    logs = fields.Nested('LogSchema', exclude=['user'], many=True)
    comments = fields.Nested('CommentSchema')#, exclude=['user'], many=True)
    class Meta:
        fields = ('id', 'email', 'username', 'password', 'is_admin', 'logs', 'comments')