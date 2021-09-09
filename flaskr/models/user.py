"""User Model."""
from flaskr import db
from werkzeug.security import check_password_hash, generate_password_hash


class UserModel(db.Model):
    """User Model."""

    __tablename__ = 'user'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(),
        nullable=False
    )
    posts = db.relationship(
        'PostModel',
        backref="author"
    )
    bookmarks = db.relationship(
        'BookmarkModel',
        backref='user'
    )

    @staticmethod
    def add(**user_data):
        """Create a new user in DB and commit it."""
        if user_data.get("id"):
            return False
        user_data['password'] = generate_password_hash(user_data['password'])
        db.session.add(
            UserModel().load(user_data)
        )
        db.session.commit()

    def verify_password(self, password):
        """Verify if this is the user's password."""
        return check_password_hash(self.password, password)

    def dump(self):
        """Serialize from model object to dict."""
        from flaskr.schemas.user import UserSchema
        return UserSchema().dump(self)

    @staticmethod
    def load(post_data):
        """Deserialize from dict to model object."""
        from flaskr.schemas.user import UserSchema
        return UserSchema().load(post_data)
