#!/usr/bin/python3
"""create a unique FileStorage instance for the application"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
