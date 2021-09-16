"""Flask App factory."""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Explicit models and schemas registration after instantiate the sqlalchemy and marshmallow modules.
from flaskr.app import models
from flaskr.app import schemas
from flaskr.app import ctrl


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",

        # store the database in the instance folder
        # DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),

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
    app.config.from_pyfile("config.py", silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the app into the sqlalchemy and marshmallow modules
    db.init_app(app)
    ma.init_app(app)

    # Initialize the app blueprint into the app
    from flaskr.app import bp
    app.register_blueprint(bp)

    return app
