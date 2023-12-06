# Import app from setup
from setup import app
from blueprints.cli_bp import db_initialise
from blueprints.users_bp import users_bp

# Register blueprint to app so can do first create and seed
app.register_blueprint(db_initialise)
app.register_blueprint(users_bp)

print(app.url_map)