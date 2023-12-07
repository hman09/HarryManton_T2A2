# Import blueprint and db for first create and seed
from flask import Blueprint
from setup import db
# thought the ma above would import the Schema but need the user model
from models.user import User
from models.log import Log

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
            username='Dave',
            email='dave@test.com',
            password='1'
        ),
        User(
            username='Gary',
            email='garr@test.com',
            password='2'
        ),
        User(
            username='Roy',
            email='roy@test.com',
            password='3'
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

    print('Seed successful')


