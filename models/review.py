#!/usr/bin/env python3
"""
Contains Review class
"""
import models
from models.user_model import UserModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Review(UserModel):
    """
    Reviews object that has reviews made

    Attributes:
        profile_id (str): has profile_id for profile being reviewed
        user_id (str): has user.id
        text (str): review text
        review_percent (float): overall percentage user was given

    """
    def __init__(self, *args, **kwargs):
        """Initialise review"""
        super().__init__(*args, **kwargs)

    if models.storage_t == "db":
        __tablename__ = "review"
        profile_id = Column(String(60), ForeignKey('profile.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False))
        text = Column(String(1024), nullable=False)
        review_percent = Column(Float, nulllanle=False)

    else:
        profile_id = ""
        user_id = ""
        text = ""
        review_percent = 0.0
