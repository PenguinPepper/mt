#!/usr/bin/env python3
"""Initialise flask app"""

from flask import Flask
from flask_backend.routes import api
from flask_jwt_extended import JWTManager


app = Flask(__name__)
api.init_app(app)

JWTManager(app)

if __name__ == "__main__":
    app.run(debug=True)
