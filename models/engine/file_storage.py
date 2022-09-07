#!/usr/bin/python3
"""
JSON instantiation class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON files to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id"""
        if obj:
            obj_dict_key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[obj_dict_key] = obj

    def save(self):
        """
        manage serialization of objects to json
        """
        new_obj = {}

        for key, value in self.__objects.items():
            new_obj[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(new_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                """value is a dict, __class__ contains the class name
                but it's a str, it can't be used as a str so
                I used eval to strip the str off"""
                cls_name = classes[(value['__class__'])](**value)
                """initialises an instance like class(**kwargs), (check
                init method of BaseModel) then passes the instance(object)
                to the 'new' method so it can be added to the __objects
                dictionary"""
                self.__objects[key] = cls_name
        except FileNotFoundError:
            pass
