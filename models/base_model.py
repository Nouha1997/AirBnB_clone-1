#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
from os import getenv

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
id = Column(String(60), nullable=False, primary_key=True, unique=True)
created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
for obj in kwargs:
if obj in ['created_at', 'updated_at']:
setattr(self, obj, datetime.fromisoformat(kwargs[obj]))
elif obj != '__class__':
setattr(self, obj, kwargs[obj])

if getenv("HBNB_TYPE_STORAGE") == 'db':
if not hasattr(kwargs, 'id'):
setattr(self, 'id', str(uuid.uuid4()))

if not hasattr(kwargs, 'created_at'):
setattr(self, 'created_at', datetime.now())

if not hasattr(kwargs, 'updated_at'):
setattr(self, 'updated_at', datetime.now())
    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
self.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict.copy()
dictionary['__class__'] = self.__classe__.__name__
for key in dictionary:
if type (dictionary[key]) is datetime:
dictionary[key]) = dictionary[key].isformat()
if '_sa_instance state' in dictionary.keys():
del dictionary['_sa_instance_state']
return dictionary

for delete(self):
"""function that delete the instance from the storage"""
from models import storage
storage.delete(self)
