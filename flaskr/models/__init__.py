"""
Force class models registration at first import.

It fixes circular dependency chains between models and schemas.
It allows to use model names as strings parameters.
It is required when schemas inports these models explicitly in the middle of a module.
"""
from flaskr.models.post import PostModel
from flaskr.models.user import UserModel
from flaskr.models.bookmark import BookmarkModel
