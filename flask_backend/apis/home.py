from flask_restx import Namespace, Resource, fields
from flask import request
from models.user import User

home_ns = Namespace('Home',
                    description="Landing page and home related operations such as signing up and loggin in ")


@home_ns.route('/')
class Home(Resource):
    """"Landing page"""

    @api.doc('Home')
    def get(self):
        pass

@home_ns.route("/login")
class HomeLogin(Resource):
    """LogIn tosite"""

    @api.doc('sign in')
    def get(self):
        pass

@home_ns.route("/signup")
class HomeSignUp(Resource):
    """Sign Up for site"""

    @api.doc('sign up')
    def post(self):
        pass
