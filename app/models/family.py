"""Family Model."""
from datetime import datetime

from app import db


class FamilyModel(db.Model):
    """Family Model."""

    __tablename__ = 'family'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    leader = db.relationship(
        'FamilyLeaderModel',
        back_populates="family",
        uselist=False
    )
    members = db.relationship(
        'UserModel',
        back_populates="family"
    )
