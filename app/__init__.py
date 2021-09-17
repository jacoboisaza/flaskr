"""Flask App factory."""
import os

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Explicit instantiate plugins and blueprint
# before impor models and schemas wich needs it.
bp = Blueprint("app", __name__)
db = SQLAlchemy()
ma = Marshmallow()


def app_factory():
    """Create and configure an instance of the Flask application."""
    new_app = Flask(__name__, instance_relative_config=False)
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

    # Initialize plugins registering the app into
    db.init_app(new_app)
    ma.init_app(new_app)

    with new_app.app_context():

        # Import my app modules
        from app import models
        from app import schemas
        from app import ctrl

        new_app.register_blueprint(bp)

    return new_app
