"""Seed file to make sample data for db"""

from models import db, Pet
from app import app

# clear and create all tables
db.drop_all()
db.create_all()

pet1 = Pet(name='Spike', 
           species='Porcupine', 
           photo_url='https://img.buzzfeed.com/buzzfeed-static/static/2014-06/26/18/enhanced/webdr04/enhanced-29284-1403820861-1.jpg',
           age=1,
           notes='Loves to talk, but gets straight to the point')
pet2 = Pet(name='The Fuzz', 
           species='Cat', 
           photo_url='https://media.istockphoto.com/id/1322123064/photo/portrait-of-an-adorable-white-cat-in-sunglasses-and-an-shirt-lies-on-a-fabric-hammock.jpg?s=612x612&w=0&k=20&c=-G6l2c4jNI0y4cenh-t3qxvIQzVCOqOYZNvrRA7ZU5o=',
           age=3,
           notes="Chillest cat you have ever seen", 
           available=False)
pet3 = Pet(name='Benjamin Buttons', 
           species='Dog', 
           photo_url='https://www.akc.org/wp-content/uploads/2017/11/Havanese-puppy.jpg',
           age=1,
           notes='I already love you, please take me home!')

db.session.add_all([pet1, pet2, pet3])
db.session.commit()