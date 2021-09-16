"""FamilyLeader Schema."""
from marshmallow_sqlalchemy import auto_field

from app.models.family_leader import FamilyLeaderModel
from app.app_factory import ma


class FamilyLeaderSchema(ma.SQLAlchemySchema):
    """Serializer for FamilyLeader Model."""

    class Meta:
        """Serializer configurations."""

        model = FamilyLeaderModel
        load_instance = True

    id = auto_field()
    leader_id = auto_field(load_only=True)
    leader = ma.Nested(
        'UserSchema',
        only=(
            'id',
            'username',
        )
    )
    family_id = auto_field(load_only=True)
    family = ma.Nested(
        'FamilySchema',
        only=(
            'id',
            'members',
        )
    )
