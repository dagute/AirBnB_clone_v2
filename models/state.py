#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String
from os import getenv
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        name = ""

    @property
    def cities(self):
        """Getter"""
        """ my_cities = [value for key, value in models.storage.all().items()
                     if 'City' in key and value.state_id == self.id] """
        all_cities = []
        for city in models.storage.all("City").values():
            if city.state_id == self.id:
                all_cities.append(city)
        return all_cities
