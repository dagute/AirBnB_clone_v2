#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Getter"""
        my_cities = [value for key, value in models.storage.all.items()
                     if 'City' in key and value.state_id = self.id]
        return my_cities
