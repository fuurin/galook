from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import sqlalchemy
import os
from .game import Game
from .games import Games

def create_app():
    app = Flask(__name__)

    api = Api(app)
    api.add_resource(Game, '/games/<int:game_id>')
    api.add_resource(Games, '/games')

    return app


app = create_app()
