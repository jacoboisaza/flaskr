"""
Implicit models registration when import this module.

It fixes circular dependency chains between models and schemas.
It allows to use model names as strings parameters.
It is required when schemas inports these models explicitly in the middle of a module.
"""
from flaskr.app.models.family import FamilyModel
from flaskr.app.models.user import UserModel
from flaskr.app.models.family_leader import FamilyLeaderModel
from flaskr.app.models.position import PositionModel
from flaskr.app.models.post import PostModel
from flaskr.app.models.bookmark import BookmarkModel
