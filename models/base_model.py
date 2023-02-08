#!/usr/bin/python3
"""Module for BaseModel"""
import uuid
from datetime import datetime

class BaseModel:
    """Base class for all other classes"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

