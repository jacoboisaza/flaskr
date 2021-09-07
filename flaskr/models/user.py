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

    @classmethod
    def add(class_, username, password):
        """Create a new user in DB and commit it."""
        new_user_model = class_(
            username=username,
            password=generate_password_hash(password)
        )
        db.session.add(new_user_model)
        db.session.commit()

    def verify_password(self, password):
        """Verify if this is the user's password."""
        return check_password_hash(self.password, password)

    def dump(self):
        """Serialize for model object."""
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_
