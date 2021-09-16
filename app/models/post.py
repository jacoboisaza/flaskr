"""Post Model."""
from flask import g
from datetime import datetime

from app.app_factory import db


class PostModel(db.Model):
    """Post Model."""

    __tablename__ = 'post'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(),
        nullable=False
    )
    body = db.Column(
        db.String(),
        nullable=False
    )
    created = db.Column(
        db.TIMESTAMP,
        nullable=False,
        default=datetime.utcnow
    )
    author_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )
    bookmarkers = db.relationship(
        'BookmarkModel',
        back_populates='post',
        cascade="all, delete-orphan"
    )
    author = db.relationship(
        'UserModel',
        back_populates="posts"
    )

    @staticmethod
    def add(**post_data):
        """Create a new post in DB and commit it."""
        if post_data.get("id"):
            return False
        post_data['author_id'] = g.user["id"]
        from app.schemas.post import PostSchema
        post_model = PostSchema().load(
            post_data
        )
        db.session.add(post_model)
        db.session.commit()

    def update(self, title, body):
        """Update a post in DB and commit it."""
        if not PostModel().query.get(self.id):
            return False
        self.title = title
        self.body = body
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete a post in DB and commit it."""
        if not PostModel().query.get(self.id):
            return False
        db.session.delete(self)
        db.session.commit()
