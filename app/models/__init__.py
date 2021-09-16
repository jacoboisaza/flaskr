"""
Implicit models registration when import this module.

It fixes circular dependency chains between models and schemas.
It allows to use model names as strings parameters.
It is required when schemas inports these models explicitly in the middle of a module.
"""
from app.models.family import FamilyModel
from app.models.user import UserModel
from app.models.family_leader import FamilyLeaderModel
from app.models.position import PositionModel
from app.models.post import PostModel
from app.models.bookmark import BookmarkModel
