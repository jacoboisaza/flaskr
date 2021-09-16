"""Family Schema."""
from marshmallow_sqlalchemy import auto_field

from flaskr.app.models.family import FamilyModel
from flaskr import ma


class FamilySchema(ma.SQLAlchemySchema):
    """Serializer for Family Model."""

    class Meta:
        """Serializer configurations."""

        model = FamilyModel
        load_instance = True

    id = auto_field()
    leader = ma.Nested(
        'FamilyLeaderSchema',
        only=(
            'id',
            'leader',
        )
    )
    members = ma.Nested(
        'UserSchema',
        many=True,
        only=(
            'id',
            'username',
        )
    )
