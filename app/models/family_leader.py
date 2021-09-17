"""FamilyLeader Model."""
from datetime import datetime

from app import db


class FamilyLeaderModel(db.Model):
    """FamilyLeader Model."""

    __tablename__ = 'family_leader'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    leader = db.relationship(
        'UserModel',
        back_populates="family_to_lead"
        # uselist=False
    )
    leader_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )
    family = db.relationship(
        'FamilyModel',
        back_populates="leader"
        # uselist=False
    )
    family_id = db.Column(
        db.Integer,
        db.ForeignKey('family.id')
    )
