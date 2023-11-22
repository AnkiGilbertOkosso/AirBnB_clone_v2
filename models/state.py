#!/usr/bin/python3
""" State Module for HBNB project"""

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
            cascade='all, delete, delete-orphan', backref="state")

    @property
    def cities(self):
        kw = models.storage.all()
        ls = []
        res = []
        for key in kw:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                ls.append(kw[key])
        for i in ls:
            if (i.state_id == self.id):
                res.append(i)
        return (res)
