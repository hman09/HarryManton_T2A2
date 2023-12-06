# can copy and paste user model and just ctrl f and replace user with log
from setup import db, ma

# Make basic Log class, just PK, Title and FK
class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50), default='Mystery Dough')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class LogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'user_id')