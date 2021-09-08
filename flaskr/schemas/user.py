"""User Schema."""
from marshmallow_sqlalchemy import auto_field

from flaskr.models.user import UserModel
from flaskr import ma


class UserSchema(ma.SQLAlchemySchema):
    """Serializer for User Model."""

    class Meta:
        """Serializer configurations."""

        model = UserModel
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    username = auto_field()
    password = auto_field()
    posts = auto_field()
