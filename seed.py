"""Seed file to make sample data for db"""

from models import db, Pet
from app import app

# clear and create all tables
db.drop_all()
db.create_all()

pet1 = Pet(name='Spike', 
           species='porcupine', 
           photo_url='https://img.buzzfeed.com/buzzfeed-static/static/2014-06/26/18/enhanced/webdr04/enhanced-29284-1403820861-1.jpg',
           age=1,
           notes='Loves to talk, but gets straight to the point')
pet2 = Pet(name='The Fuzz', 
           species='cat', 
           photo_url='https://static.boredpanda.com/blog/wp-content/uploads/2015/12/fluffy-cat-funny-pics-35__605.jpg',
           age=1, 
           available=False)

db.session.add_all([pet1, pet2])
db.session.commit()