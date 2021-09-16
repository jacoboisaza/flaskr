"""Position Schema."""
from marshmallow_sqlalchemy import auto_field

from flaskr.app.models.position import PositionModel
from flaskr import ma


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
