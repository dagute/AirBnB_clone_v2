#!/usr/bin/python3
"""DBstorage"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def get_url():
    """Get url for the engine"""

    value = os.getenv("HBNB_MYSQL_USER")
    value1 = os.getenv("HBNB_MYSQL_PWD")
    value2 = os.getenv("HBNB_MYSQL_HOST")
    value3 = os.getenv("HBNB_MYSQL_DB")
    # drop tables if HBNB_ENV = test
    value4 = os.getenv("HBNB_ENV")

    if value4 = "test":
        Base.metadata.drop_all(self.__engine)

    u = "mysql+pymysql://{}:{}@{}:3306/{}"\
        .format(value, value1, value2, value3)

    return u


class DBstorage():
    """Engine Creator"""
    __engine = None
    __session = None

    def __init__(self):
        """Init"""
        self.__engine = create_engine(get_url(), pool_pre_ping=True)

    def all(self, cls=None):
        """ALL function"""
        new_dict = {}
        if cls is not None:
            for data in self.__session.query(cls).all():
                key = str(cls) + "." + str(data.id)
                new_dict[key] = data.__dict__
            return new_dict

        else:
            my_class = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

            for idx_class in my_class:
                rows = self.__session.query(idx_class).all()
                for data_convert in rows:
                    key = idx_class + "." + str(data_convert.id)
                    new_dict[key] = data_convert.__dict__
                return new_dict

    def new(self, obj):
        """Function that add new objects in current session"""
        self.__session.add(obj)

    def save(self):
        """Commit all the changes in the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete objects from the current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
            create the current database session
        """
        Session_new = sessionmaker(expire_on_commit=False)
        Session_new.configure(bind=self.__engine)
        Session = scoped_session(session_new)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)
