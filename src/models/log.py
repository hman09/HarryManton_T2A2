# can copy and paste user model and just ctrl f and replace user with log
from setup import db, ma
from marshmallow import fields


# Make basic Log class, just PK, Title and FK
class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50), default='Mystery Dough')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='logs')
    comments = db.relationship('Comment', back_populates='logs')


class LogSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['username', 'id'])
    comments = fields.Nested('CommentSchema', only=['message', 'user_id'], many=True)
    class Meta:
        fields = ('id', 'title', 'user_id', 'user', 'comments')