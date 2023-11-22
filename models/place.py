#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from os import getenv
import models

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
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete=orphan',
                               backref="place"
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=false,
                                 back_populate="place_amenities")
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            var = models.storage.all()
            lists = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    lists.append(var[key])
            for lem in lists:
                if (lem.place_id == self.id):
                    result.append(lem)
            return (result)

        @property
        def amenities(self):
            """ Returns list of amenities.ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
