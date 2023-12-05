# Import blueprint and db for first create and seed
from flask import Blueprint
from setup import db, ma

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
            username='user1',
            email='user1@test.com'
        ),
        User(
            username='user2',
            email='user2@test.com'
        ),
        User(
            username='user3',
            email='user3@test.com'

        )
    ]


