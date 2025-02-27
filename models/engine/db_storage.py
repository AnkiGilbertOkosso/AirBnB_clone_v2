#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(user, passwd, host, db),
                pool_pre_ping=True
        )
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        """
        diction = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            kw = self.__session.query(cls)
            for i in kw:
                key = "{}.{}".format(type(i).__name__, i.id)
                diction[key] = i
        else:
            ls = [State, City, User, Place, Review, Amenity]
            for clase in ls:
                kw = self.__session.query(clase)
                for i in kw:
                    key = "{}.{}".format(type(i).__name__, i.id)
                    diction[key] = i
        return (diction)

    def new(self, obj):
        """add an element to the table"""
        self.__session.add(obj)

    def save(self):
        """save any change"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        make_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(make_session)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
