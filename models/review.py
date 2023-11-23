#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.places import Place
from models.user import User


class Review(BaseModel, Base):
    """ Review class to store review information
    Attributes:
        tablename: represents the table name
        text: review
        place_id: place id
        user_id: user id
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=false)
        place_id = Column(String(60), nullable=false, ForeignKey("places.id"))
        user_id = Column(String(60), nullable=false, ForeignKey("users.id"))

    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
