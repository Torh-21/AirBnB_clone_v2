#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes
    Attributes:
        email: user's email
        password: user password
        first_name: user's first name
        last_name: user's last name
        palces: Represent a relationship between the User and Place class
        reviews: Represent a relationship between the User and Review class
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade='all, delete', backref='user')
    reviews = relationship("Review", cascade='all, delete', backref='user')
