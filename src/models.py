import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

#user, characters, planets, favorites,

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True) 
    character_name = Column(String(250), nullable=False)
    character_info = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_characters = relationship(User)

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True) 
    planet_name = Column(String(250), nullable=False)
    planet_info = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_planets = relationship(User)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True) 
    fav_planets = Column(String(250), nullable=False)
    num_fav_planets = Column(Integer, nullable=False)
    fav_characters = Column(String(250), nullable=False)
    num_fav_characters = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_favorites = relationship(User)
    rel_with_planets = relationship(Planets)
    rel_with_characters = relationship(Characters)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')