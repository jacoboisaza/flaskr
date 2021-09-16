"""Position Model."""
from flask import g
from datetime import datetime

from flaskr import db


class PositionModel(db.Model):
    """Position Model."""

    __tablename__ = 'position'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    person_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )
    person = db.relationship(
        'UserModel',
        back_populates="position"
    )
