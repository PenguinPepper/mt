from flask import Flask
from apis import api
from flask_jwt_extened import JWTManager

app = Flask(__name__)
api.init_app(app)

JWTManager(app)
