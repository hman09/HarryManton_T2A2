# copy and paste comment and alter (should have used logs for the FK)
# comment out back-populates for future use
from setup import db, ma
from marshmallow import fields


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)

    message = db.Column(db.String(250), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    log_id = db.Column(db.Integer, db.ForeignKey('logs.id'), nullable=False)

    logs = db.relationship('Log', back_populates='comments')
    user = db.relationship('User', back_populates='comments')


class CommentSchema(ma.Schema):
    logs = fields.Nested('LogSchema', only=['title'])
    user = fields.Nested('UserSchema', only=['id', 'username'])
    class Meta:
        fields = ('id','message', 'user_id', 'log_id', 'logs', 'user')