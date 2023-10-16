#!/usr/bin/python3
"""Definition of the BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the Basemodel class for Airbnb project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel"""

        self.id = self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        dformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Return str representation of the BaseModel instance"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
