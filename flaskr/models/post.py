"""Post Model."""
from flask import g
from datetime import datetime
from sqlalchemy import desc

from flaskr import db


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

    def dump(self):
        """Serialize from model object to dict."""
        from flaskr.schemas.post import PostSchema
        return PostSchema().dump(self)


    @staticmethod
    def add(**post_data):
        """Create a new post in DB and commit it."""
        if PostModel().query.get(post_data.get("id")):
            return False
        post_data['author_id'] = g.user["id"]
        db.session.add(
            PostModel().load(post_data)
        )
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

    @staticmethod
    def load(post_data):
        """Deserialize from dict to model object."""
        from flaskr.schemas.post import PostSchema
        return PostSchema().load(post_data)
