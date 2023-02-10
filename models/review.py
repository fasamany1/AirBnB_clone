#!/usr/bin/python3
"""
module that contain the Review class

Class:
    Review : define Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
