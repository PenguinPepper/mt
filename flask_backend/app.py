#!/usr/bin/env python3
"""Initialise flask app"""

from flask import Flask
from flask_backend.routes import api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from os import getenv

load_dotenv()
secret_key = getenv('SECRET_KEY')

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = secret_key
api.init_app(app)

JWTManager(app)

if __name__ == "__main__":
    app.run(debug=True)
