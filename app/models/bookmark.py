"""Bookmark Model."""
from datetime import datetime

from app import db


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
        db.ForeignKey('user.id'),
    )
    post_id = db.Column(
        db.Integer,
        db.ForeignKey('post.id'),
    )
    user = db.relationship(
        'UserModel',
        back_populates='bookmarks',
    )
    post = db.relationship(
        'PostModel',
        back_populates='bookmarkers'
    )
