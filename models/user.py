#!/usr/bin/env python3
"""
Contains the user class
"""

import models
from models.user_model import UserModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(UserModel, Base):
    """
    Class for users

    Attributes:
        __init__(): initialises the reiew object
        email (str): contains email of user
        password (str): contains password for profile
        first_name (str): name of user
        last_name (str): last name of user
        cohort_no (int): cohort that user belongs to.
    """

    if models.storage_t == "db":
        __tablename__ = 'users'
        email = Column(String(120), nullable=False)
        password = Column(String(120), nullable=False)
        first_name = Column(String(120), nullable=False)
        last_name = Column(String(120), nullable=False)
        profile_id = Column(String(120), Foreignkey(profile.id), nullable=False)
        github_usr_name=Column(String(120), nullable=False)
        cohort_no = Column(Integer, nullable=False)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        github_usr_name = ""
        cohort_no = 0

     def __init__(self, *args, **kwargs):
        """Initialise User"""
        super().__init__(*args, **kwargs)
