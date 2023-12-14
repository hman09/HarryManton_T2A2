# Import blueprint and db for first create and seed
from flask import Blueprint
from setup import db, bcrypt
# thought the ma above would import the Schema but need the user model
from models.user import User
from models.log import Log
from models.comment import Comment
from models.recipe import Recipe

# Define Blueprint
db_initialise = Blueprint('db', __name__)

# Create database
@db_initialise.cli.command('create')
def create():
    # use drop then create to reset db. add print "DB reset" to test command
    db.drop_all()
    db.create_all()
    print('DB reset')

# Seed database
@db_initialise.cli.command('seed')
def seed():
    # Will need to make Schema for User to insert -- DONE
    # Make 3 users just need username and email for now
    users = [
        User(
            username='Admin',
            email='admin@test.com',
            password=bcrypt.generate_password_hash('admin').decode("utf8"),
            is_admin=True
        ),
        User(
            username='Gary',
            email='gary@test.com',
            password=bcrypt.generate_password_hash('gary').decode("utf8"),
        ),
        User(
            username='Roy',
            email='roy@test.com',
            password=bcrypt.generate_password_hash('roy').decode("utf8"),
        )
    ]
    db.session.add_all(users)
    db.session.commit()

    # Seeding 6 Logs 2 for each user
    logs = [
        Log(
            title="Wholemeal",
            user_id = users[0].id
        ),
        Log(
            title="White",
            user_id = users[0].id  
        ),
        Log(
            title="Baguette",
            user_id = users[1].id
        ),
        Log(
            title="Sourdough",
            user_id = users[1].id
        ),
        Log(
            title="Pizza",
            user_id = users[2].id
        ),
        Log(
            title="Brioche",
            user_id = users[2].id
        )
    ]
    db.session.add_all(logs)
    db.session.commit()

    comments = [
        Comment(
            message = "I love Pizza!",
            user_id = users[1].id,
            log_id = logs[4].id
        ),
        Comment(
            message = "So do I, Try my recipes its Great!",
            user_id = users[2].id,
            log_id = logs[4].id
        )
    ]
    db.session.add_all(comments)
    db.session.commit()

    recipe = [
        Recipe(
            flour_types = 'White',
            flour_g = 1000,
            water_g = 700,
            starter_type = 'Dry Yeast',
            bulk_fermentation_min = 120,
            knead = 'Mixer',
            log_id = logs[2].id
        )
    ]
    db.session.add_all(recipe)
    db.session.commit()

    

    print('Seed successful')

