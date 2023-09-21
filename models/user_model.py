#!/usr/bin/env python3
"""
Contains Base Model class that the other classses will inherit from
"""


import models
from datetime import datetime
from uuid import uuid4
from dotenv import load_dotenv
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

time = "%Y-%m-%dT%H:%M:%S.%f"
if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class UserModel:
    """
    Class from which future classes that will be
    used for Conn-laison will inherit from.

    Attributes:
        save(): updates datetime at updated_at
        to_dict(): returns a dictionary of all key value pairs of instance
        delete(): deletes the instance frnm stoage
    """
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.now)
        updated_at = Column(DateTime,default=datetime.now)

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel Object

        Attributes:
            id (str): Unique Instance id
            created_at (datetime): Assign datetime Values
            updated_at (datetime): Update datetime Values
            kwargs (dict): Serialized Instance
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """"Return string representation of instance"""
        name = self.__class__.__name__
        attrs = self.__dict__
        return f"[{name}] ({self.id}) {attrs}"

    def save(self):
        """Updates the updated_at attribute"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict

    def delete(self):
        """"Deletes instance"""
        models.storage.delete(self)
