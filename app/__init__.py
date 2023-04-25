from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
import os

from .models import db
from .resources.Evento import Evento

load_dotenv()


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config["MONGODB_SETTINGS"] = {
        'host': os.getenv('URI')
    }

    db.init_app(app)

    # Routes
    api.add_resource(Evento, '/')

    return app
