#!/usr/bin/env python3

from flask_restx import Namespace, Resource, fields
from flask import request, make_response, jsonify
from models.user import User
from models import storage
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token

#JWTManager(app)

home_ns = Namespace('Home',
                    description="Landing page and home related operations such as signing up and loggin in ")

sign_up = home_ns.model('SignUp', {
    'name': fields.String(),
    'surname': fields.String(),
    'email': fields.String(),
    'password': fields.String(),
    'github_name': fields.String(),
    'çohort_no': fields.Integer()
    })

login = home_ns.model('LogIn', {
    'email': fields.String(),
    'password': fields.String()
    })

@home_ns.route('/')
class Home(Resource):
    """"Landing page"""

    @home_ns.doc('Home')
    def get(self):
        pass

@home_ns.route("/login")
class HomeLogin(Resource):
    """LogIn tosite"""

    @home_ns.doc('sign in')
    @home_ns.expect(login)
    def post(self):
        data = request.get_json()

        email_address = data.get('email')
        password = data.get('password')

        db_user = storage.search(User, email, email_address)

        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.email)
            refresh_token = create_refresh_token(identity=db_user.email)

        return jsonify(
                {'access_token': acess_token,
                 'refrsh_token': refresh_token}
                )

        

@home_ns.route("/signup")
class HomeSignUp(Resource):
    """Sign Up for site"""

    @home_ns.doc('sign up')
    @home_ns.expect(sign_up)
    def post(self):
        data = request.get_json()

        user_info = {'name': data.get('name'),
                'surname': data.get('surname'),
                'email': data.get('email'),
                'password': generate_password_hash(data.get('password')),
                'github_name': data.get('github_name'),
                'cohort_no': data.get('cohort_no')
                }

        new_user = User(**user_info)
        new_user.save()

        return make_response(jsonify({"message": "Profile sucessfully created proceed to login"}), 201)
