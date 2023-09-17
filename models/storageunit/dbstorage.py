#!/usr/bin/env python3
"""Contains database class"""


import models
from models.user_model import UserModel
from models.review import Review
from models.user import User
from dotenv import load_dotenv
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv()
classes = {"UserModel": UserModel, "Review": Review, "User": User}

class DBstorage:
    """Saves classes to Database"""
    __engine = None
    __session = None

    def __init__(self):
        """Ïnitiate db storage"""
        MISSION_T_MYSQL_USER = getenv('MISSION_T_MYSQL_USER')
        MISSION_T_PWD = getenv('MISSION_T_PWD')
        MISSION_T_MYSQL_HOST = getenv('MISSION_T_MYSQL_HOST')
        MISSION_T_DB = getenv('MISSION_T_DB')
        cmd = f"mysql+mysqldb://{MISSION_T_MYSQL_USER}:\
                {MISSION_T_PWD}@{MISSION_T_MYSQL_HOST}/{MISSION_T_DB}"
        self.__engine = create_engine(cmd)

    def all(self, cls=None):
        """
        Query database session objects depending on class

        Args:
            cls(object): class to be queried
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """
        Add object to database session

        Args:
            obj(object): object to be added to session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all database changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete current database session if db is None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create current database from from sessions and tables ib database
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        """
        self.__session.remove()

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
