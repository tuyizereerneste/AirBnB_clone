#!/usr/bin/python3
"""Definition of the FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents the FileStorage class
    Arguments:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            objdict = {
                    key: obj.to_dict()
                    for key, obj in FileStorage.__objects.items()
            }
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)"""
        try:
            with open(FileStorage.__file_path) as f:
                odict = json.load(f)
                for v in odict.values():
                    cls_name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(cls_name)(**v))
        except FileNotFoundError:
            return
