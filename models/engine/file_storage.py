#!/usr/bin/python3
"""Module for FileStorage class"""
import json
import os


class FileStorage:
    """Class for storing and retrieving data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file"""
        with open(FileStorage.__path, "w", encoding="utf-8") as file:
            d = {k: val.to_dict() for k, val in FileStorage.__objects.items()}
            json.dump(dict_objs, file)

    def reload(self):
        """Reloads the stored objects"""

        from models.base_model import BaseModel
        classes = {
                'BaseModel': BaseModel
                }
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            obj_dict = {key: classes[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict
