#!/usr/bin/env python3
"""
Contains the user class
"""

import models
from models.user_model import UserModel, Base
from os import getenv
from uuid import uuid4
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Profile(UserModel, Base):
    """Class for User profile"""
     def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        self.profile_id = str(uuid4())

    if model.storage_t == "db":
        __tablename__ = "profile"
        about = Column(String(125), nullable=True)
        dp_id = Column(Integer, nullable=False, default=0)
        profile_id = Column(String(128), primary_key=True, nullable=False)

    about = ""
    dp_id = 0
