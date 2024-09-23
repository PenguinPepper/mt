#!/usr/bin/env python3

from flask_restx import Namespace, Resource, fields
from flask import request, make_response, jsonify
from models.user import User
from models import storage
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager,
        jwt_required, create_access_token, 
        create_refresh_token, get_jwt_identity)

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


@home_ns.route("/login")
class HomeLogin(Resource):
    """LogIn tosite"""

    @home_ns.doc('Log In')
    @home_ns.expect(login)
    def post(self):
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        db_user = storage.search(User, email)

        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.email)
            refresh_token = create_refresh_token(identity=db_user.email)

            return jsonify(
                {'access_token': access_token,
                 'refrsh_token': refresh_token}
                )
        else:
            return make_response(jsonify({"message": "Invalid username or password"}), 403)

        

@home_ns.route("/refresh")
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)

        return make_response(jsonify({"access_token": new_access_token}), 200)
