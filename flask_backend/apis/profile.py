from flask_restx import Namespace, Resource, fields
from flask import request
from models.user import User

profile_ns = Namespace('Profile',
                       description='Profile related operations')

@profile_ns.route("/profile/update")
class ProfileUpdate(Resource):
    """Üpdate your profile"""

    @api.doc(description="Updateyour profile")
    def put(self):
        """Update profile infromation"""
        pass

@profile_ns.route("/profile/delete")
class ProfileDelete(Resource):
    """"Delete logged in users profile"""

    @api.doc(description="Delete logged in users profile")
    def delete(self):
        """Delete profile"""
        pass
