"""Bookmark Schema."""
from marshmallow_sqlalchemy import auto_field

from flaskr.models.bookmark import BookmarkModel
from flaskr import ma


class BookmarkSchema(ma.SQLAlchemySchema):
    """Serializer for Bookmark Model."""

    class Meta:
        """Serializer configurations."""

        model = BookmarkModel
        load_instance = True
        datetimeformat = '%Y-%m-%d'

    id = auto_field()
    created = auto_field()
    user = ma.Nested(
        "UserSchema",
        only=(
            'id',
            'username',
        )
    )
    post = ma.Nested(
        "PostSchema",
        only=(
            'id',
            'title',
            'body',
            'created',
            'author',
        )
    )
