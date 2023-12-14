from setup import app
from blueprints.cli_bp import db_initialise
from blueprints.users_bp import users_bp

app.register_blueprint(db_initialise)
app.register_blueprint(users_bp)

# Endpoint Printout
# print(app.url_map)