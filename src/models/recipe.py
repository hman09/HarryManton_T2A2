from setup import db, ma
from marshmallow import fields


# Make basic Recipe class, just PK, Title and FK
class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)

    flour_types = db.Column(db.String(50), default='')
    flour_g = db.Column(db.Integer, nullable=False)
    water_g = db.Column(db.Integer, nullable=False)
    starter_type = db.Column(db.String(50), default='')
    starter_g = db.Column(db.Integer, default=0)
    bulk_fermentation_min = db.Column(db.Integer, nullable=False)
    knead = db.Column(db.String(50), default='')

    log_id = db.Column(db.Integer, db.ForeignKey('logs.id'), nullable=False)

    logs = db.relationship('Log', back_populates='recipe')


class RecipeSchema(ma.Schema):
    #logs = fields.Nested('LogSchema', only=['title'])
    class Meta:
        fields = ('id', 'flour_type', 'flour_g','water_g','starter_type', 'starter_g','bulk_fermentation_min', 'knead', 'log_id')