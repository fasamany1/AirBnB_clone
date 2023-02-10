#!/usr/bin/python3
"""
module that contain the User class

Class:
    User : define User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
