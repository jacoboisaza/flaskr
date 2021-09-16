"""
Implicit class schemas registration when import this module.

It fixes circular dependency chains between models and schemas.
It allows to use schama names as strings parameters.
It is required when models inports these schemas explicitly in the middle of a module.
"""
from app.schemas.family import FamilySchema
from app.schemas.user import UserSchema
from app.schemas.family_leader import FamilyLeaderSchema
from app.schemas.position import PositionSchema
from app.schemas.post import PostSchema
from app.schemas.bookmark import BookmarkSchema
