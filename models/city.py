#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base 
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
__tablename__ = 'cities'
if getenv("HBNB_TYPE_STORAGE") == 'db':
name = Column(String(128), nullable=False)
state_id  = Column(string(60), ForeignKey('states.id'), nullable=False)
places = relationship('place', backref='cities', 
cascades='all, delete, delete-orphan')
else:
    state_id = ""
    name = ""
