"""User Model."""
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr import db


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
        back_populates="author",
        cascade="all, delete-orphan"
    )
    bookmarks = db.relationship(
        'BookmarkModel',
        back_populates='user',
        cascade="all, delete-orphan"
    )
    position = db.relationship(
        'PositionModel',
        back_populates="person",
        uselist=False
    )
    family_id = db.Column(
        db.Integer,
        db.ForeignKey('family.id')
    )
    family = db.relationship(
        'FamilyModel',
        back_populates="members"
    )
    family_to_lead = db.relationship(
        'FamilyLeaderModel',
        back_populates="leader",
        uselist=False
    )

    @staticmethod
    def add(**user_data):
        """Create a new user in DB and commit it."""
        if user_data.get("id"):
            return False
        user_data['password'] = generate_password_hash(user_data['password'])
        from flaskr.app.schemas.user import UserSchema
        user_model = UserSchema().load(user_data)
        db.session.add(user_model)
        db.session.commit()

    def verify_password(self, password):
        """Verify if this is the user's password."""
        return check_password_hash(self.password, password)
