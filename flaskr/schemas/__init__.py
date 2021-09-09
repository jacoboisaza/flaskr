"""
Force class schemas registration at first import.

It fixes circular dependency chains between models and schemas.
It allows to use schama names as strings parameters.
It is required when models inports these schemas explicitly in the middle of a module.
"""
from flaskr.schemas.post import PostSchema
from flaskr.schemas.user import UserSchema
from flaskr.schemas.bookmark import BookmarkSchema
