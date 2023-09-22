#!/usr/bin/env python3
"""
Contains Filestorage class that saves the instances in JSON form
"""

import json
import models
from models.user_model import UserModel
from models.review import Review
from models.user import User

classes = {"UserModel": UserModel, "Review": Review, "User": User}


class Filestorage:
    """Serialises insgance to a JSON file and deselialise it."""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """
        Populates __objects in {<obj class name>.id: obj}
            format.
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def reload(self):
        """deserialize JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def save(self):
        """serialiazes __objects to the JSON file (path: __file_path)"""
        ser_object = {}
        for key in self.__objects:
            ser_object[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(ser_object, f)

    def reloads(self):
        """deserliases JSON objects from a file"""
        try:
            with open(self.__file_path, 'r') as f:
                norm_obj = json.load(f)
            for key in norm_obj:
                self.__objects[key] = classes[norm_obj[key]
                                              ["__class__"]](**norm_obj[key])
        except Exception as err:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
        if key in self.__objects:
            del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """
        Retrieves an object based on the class and ID.

        Args:
            cls (class): The class of the object to retrieve.
            id (str): The ID of the object.

        Returns:
            The retrieved object if found, or None if not found.
        """
        if cls in classes.values() and isinstance(id, str):
            objects = self.all(cls)
            for key, value in objects.items():
                if key.split(".")[1] == id:
                    return value
        return None

    def count(self, cls=None):
        """
        Count the number of items in the dataset.

        Args:
            cls (optional): The class to filter the dataset.
            If None, count all items.

        Returns:
            int: The count of items in the dataset.

        """
        return len(self.all(cls))
