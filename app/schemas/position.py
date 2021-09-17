"""Position Schema."""
from marshmallow_sqlalchemy import auto_field

from app.models.position import PositionModel
from app import ma


class PositionSchema(ma.SQLAlchemySchema):
    """Serializer for Position Model."""

    class Meta:
        """Serializer configurations."""

        model = PositionModel
        load_instance = True

    id = auto_field()
    person_id = auto_field(load_only=True)
    person = ma.Nested(
        'UserSchema',
        only=(
            'id',
            'username',
        )
    )
