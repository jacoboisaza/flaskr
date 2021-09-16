"""
Implicit class schemas registration when import this module.

It fixes circular dependency chains between models and schemas.
It allows to use schama names as strings parameters.
It is required when models inports these schemas explicitly in the middle of a module.
"""
from flaskr.app.schemas.family import FamilySchema
from flaskr.app.schemas.user import UserSchema
from flaskr.app.schemas.family_leader import FamilyLeaderSchema
from flaskr.app.schemas.position import PositionSchema
from flaskr.app.schemas.post import PostSchema
from flaskr.app.schemas.bookmark import BookmarkSchema
