"""Flask App factory."""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Explicit instantiate the sqlalchemy and marshmallow modules
# before models and schemas wich needs it.
db = SQLAlchemy()
ma = Marshmallow()

from app import models
from app import schemas
from app import ctrl


def create_app():
    """Create and configure an instance of the Flask application."""
    new_app = Flask(__name__, instance_relative_config=True)
    new_app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",

        DATABASE={
            'dbname': 'flaskr',
            'user': 'postgres',
            'password': 'mypass',
            'host': 'localhost',
            'port': '5432',
        },

        SQLALCHEMY_DATABASE_URI='postgresql://postgres:mypass@localhost:5432/flaskr',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,

    )
    new_app.config.from_pyfile("config.py", silent=True)

    # ensure the /instance folder exists
    try:
        os.makedirs(new_app.instance_path)
    except OSError:
        pass

    # register the app into the sqlalchemy and marshmallow modules
    db.init_app(new_app)
    ma.init_app(new_app)

    # Initialize the app blueprint into the new_app
    from app import bp
    new_app.register_blueprint(bp)

    return new_app
