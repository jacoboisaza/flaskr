"""Post Schema."""
from marshmallow_sqlalchemy import auto_field

from app.models.post import PostModel
from app.app_factory import ma


class PostSchema(ma.SQLAlchemySchema):
    """Serializer for Post Model."""

    class Meta:
        """Serializer configurations."""

        model = PostModel
        load_instance = True
        datetimeformat = '%Y-%m-%d'

    id = auto_field()
    title = auto_field()
    body = auto_field()
    created = auto_field()
    bookmarkers = ma.Nested(
        'BookmarkSchema',
        many=True,
        only=(
            'id',
            'created',
            'user',
        )
    )
    author_id = auto_field(load_only=True)
    author = ma.Nested(
        'UserSchema',
        only=(
            'id',
            'username',
        )
    )
