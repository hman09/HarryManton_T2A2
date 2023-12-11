# copy and paste comment and alter (should have used logs for the FK)
# comment out back-populates for future use
from setup import db, ma
from marshmallow import fields


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)

    comment = db.Column(db.String(250), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    log_id = db.Column(db.Integer, db.ForeignKey('logs.id'), nullable=False)

    # logs = db.relationship('Log', back_populates='comment')


class CommentSchema(ma.Schema):
    # logs = fields.Nested('LogSchema', exclude=['comment'], many=True)
    class Meta:
        fields = ('id','comment', 'user_id', 'log_id')