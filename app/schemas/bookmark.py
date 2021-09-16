"""Bookmark Schema."""
from marshmallow_sqlalchemy import auto_field

from app.models.bookmark import BookmarkModel
from app.app_factory import ma


class BookmarkSchema(ma.SQLAlchemySchema):
    """Serializer for Bookmark Model."""

    class Meta:
        """Serializer configurations."""

        model = BookmarkModel
        load_instance = True
        datetimeformat = '%Y-%m-%d'

    id = auto_field()
    created = auto_field()
    user_id = auto_field(load_only=True)
    user = ma.Nested(
        "UserSchema",
        only=(
            'id',
            'username',
        )
    )
    post_id = auto_field(load_only=True)
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
