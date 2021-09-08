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
        """Serialize model object."""
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_

    @staticmethod
    def add(title, body):
        """Create a new post in DB and commit it."""
        new_post_model = PostModel(
            title=title,
            body=body,
            author_id=g.user["id"]
        )
        db.session.add(new_post_model)
        db.session.commit()

    @staticmethod
    def update(post_id, title, body):
        """Update a post in DB and commit it."""
        post_model = PostModel.query.get(post_id)
        post_model.title = title
        post_model.body = body
        db.session.add(post_model)
        db.session.commit()

    @staticmethod
    def delete(post_id):
        """Delete a post in DB and commit it."""
        post_model = PostModel.query.get(post_id)
        db.session.delete(post_model)
        db.session.commit()

    @staticmethod
    def all_by_user_id(author_id):
        """Get all posts filtered by author_id."""
        return PostModel.query.filter(
            PostModel.author_id == author_id
        ).order_by(
            desc(PostModel.created)
        ).all()
