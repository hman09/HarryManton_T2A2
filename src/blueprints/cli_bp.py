# Import blueprint and db for first create and seed
from flask import Blueprint
from setup import db
# thought the ma above would import the Schema but need the user model
from models.user import User

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
            email='dave@test.com'
        ),
        User(
            username='Gary',
            email='garr@test.com'
        ),
        User(
            username='Roy',
            email='roy@test.com'
        )
    ]
    # Commit session to db, print Seed successful
    db.session.add_all(users)
    db.session.commit()
    print('Seed successful')
    


