#!/usr/bin/python3
"""
module that contain the Amenity class

Class:
    Amenity : define Amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for managing amenity objects"""

    name = ""
