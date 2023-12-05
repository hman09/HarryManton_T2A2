# Import db and schema
from setup import db, ma

# Make basic User class, just PK, email and username for now
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)

# Use above for marshmallow
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'username')