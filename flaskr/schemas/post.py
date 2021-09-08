"""Post Schema."""
from marshmallow_sqlalchemy import auto_field

from flaskr.models.post import PostModel
from flaskr import ma


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
    author_id = auto_field()
