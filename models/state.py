#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
if getenv("HBNB_TYPE_STORAGE") == 'db':
name = Column(String(128), nullable=False)
cities = relationship('city', backref='state',
cascade='all, delete, delete-orphan')

else:
name = ""

@property
def cities(self):
"""relationship between city and state"""
from models import storage
new_city = []
all_cities = storage.all(city)
for city in all_cities.values():
if city.state_id == self.id:
new_city.append(city)
return new_city
