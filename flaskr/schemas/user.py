"""User Schema."""
from marshmallow_sqlalchemy import auto_field

from flaskr.models.user import UserModel
from flaskr import ma


class UserSchema(ma.SQLAlchemySchema):
    """Serializer for User Model."""

    class Meta:
        """Serializer configurations."""

        model = UserModel
        load_instance = True

    id = auto_field()
    username = auto_field()
    password = auto_field(load_only=True)
    bookmarks = ma.Nested(
        'BookmarkSchema',
        many=True,
        only=(
            'id',
            'created',
            'post',
        )
    )
    posts = ma.Nested(
        'PostSchema',
        many=True,
        only=(
            'id',
            'title',
            'body',
            'created',
        )
    )
