# Import app from setup
from setup import app
from blueprints.cli_bp import db_initialise

# Register blueprint to app so can do first create and seed
app.register_blueprint(db_initialise)