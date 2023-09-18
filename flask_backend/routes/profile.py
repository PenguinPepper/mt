#!/usr/bin/env python3

from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import jwt_required
from models.user import User

profile_ns = Namespace('Profile',
                       description='Profile related operations')

@profile_ns.route("/profile/update")
class ProfileUpdate(Resource):
    """Üpdate your profile"""

    @jwt_required()
    def put(self):
        """Update profile infromation"""
        pass

@profile_ns.route("/profile/delete")
class ProfileDelete(Resource):
    """"Delete logged in users profile"""

    @jwt_required()
    def delete(self):
        """Delete profile"""
        pass
