"""Bookmark Model."""
from flask import g
from datetime import datetime
from sqlalchemy import desc

from flaskr import db


class BookmarkModel(db.Model):
    """Bookmark Model."""

    __tablename__ = 'bookmark'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    created = db.Column(
        db.TIMESTAMP,
        nullable=False,
        default=datetime.utcnow
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )
    post_id = db.Column(
        db.Integer,
        db.ForeignKey('post.id')
    )

    def dump(self):
        """Serialize from model object to dict."""
        from flaskr.schemas.bookmark import BookmarkSchema
        return BookmarkSchema().dump(self)

    @staticmethod
    def load(bookmark_data):
        """Deserialize from dict to model object."""
        from flaskr.schemas.bookmark import BookmarkSchema
        return BookmarkSchema().load(bookmark_data)
