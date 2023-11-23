#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from os import getenv
import models

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay
    Attributes:
        tablename: the table name
        city_id: city id
        user_id: user id
        name: city name
        description: place description
        number_rooms: number of rooms
        number_bathrooms: number of bathrooms
        max_guest: max number of guests allowed
        price_by_night: daily price
        latitude: latitude (float)
        longitude: longitude (float)
        reviews: represents a relationship with the Review class
    """

   amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), nullable=false, ForeignKey('cities.id'))
        user_id = Column(String(60), nullable=false, ForeignKey('users.id'))
        name = Column(String(128), nullable=false)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=false, default=0)
        number_of_bathrooms = Column(Integer, nullable=false, default=0)
        max_guest = Column(Integer, nullable=false, default=0)
        price_by_night = Column(Integer, nullable=false, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", cascade='all, delete, delete=orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=false,
                                 back_populate="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """ Returns list of reviews.id """
         values_review = models.storage.all("Review").values()
        list_review = []
        for review in values_review:
            if review.place_id == self.id:
                list_review.append(review)
        return list_review

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """attribute that returns list of Amenity instances"""
            values_amenity = models.storage.all("Amenity").values()
            list_amenity = []
            for amenity in values_amenity:
                if amenity.place_id == self.id:
                    list_amenity.append(amenity)
            return list_amenity
