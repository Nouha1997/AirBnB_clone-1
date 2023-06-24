#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
from sqlalchemy.sql.schema import Table
from models.amenity import Amenity 
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == 'db':
place_amenity = Table('place_amenity', Base.metadata,
Column('place_id', String(60),
ForeignKey('places.id'),
primary_key=True, nullable=False),
Column('amenity_id', String(60),
ForeignKey('amenities.id'),
primary_key=True, nullable=Fslse))

class Place(BaseModel, Base):
    """ A place to stay """
__tablename__ = 'places'
if getenv("HBNB_TYPE_STORAGE") == 'db':
city_i d= Column(String(60), ForeignKey('cities.id'), nullable=False)
user_id = Column(string(60), ForeignKey('users.id'), nullable=False)
name = Column(stuing(128), nullable=False)
description = Column(string(1024), nullable=True)
number_rooms = Column(Integer, default=0, nullable=False)
number_bathrooms = Column(Integer, default=0, nullable=False)
max_guest = Column(Integer, default=0, nullable=False)
price_by_night = Column(Integer, default=0, nullable=False)
latitude = Column(Float, nullable=True)
longitude = Column(Float, nullable=True)
reviews = relationship('Review', backref='place',
cascade='all, delete, delete-orphan')
amenities = relationship('Amenity', secondary=place_amenity,
viewonly=False, backref='place_amenities')
else: 
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

@property
def reviews(self):
"""returns list of review instances with place_id"""
form models import storage
all_reviews = storage.all(Review)
r_list = []
for review in all_review.values():
if revie.place_id == self.id:
r_list.append(review)
return r_list

@property
def amenities(self):
"""returns the list of Amenity instances"""
from models import storage
all_amenities = storage.sll(Amenity)
a_list = []
for amenity in all_amenities.values():
if amenity.id in self.amenity_ids:
a_list.append(amenity)
return a_list


@amenities.stter
def amenities(self, obj):
"""method for adding an Amenity.id """
if obj is not None:
if isinstance(obj, Amenity):
if obj.id not in self.amenity_ids:
self.amenity_ids.append(obj.id)
