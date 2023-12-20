import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String, unique=False, nullable=False)
    firstname = Column(String(20),nullable=False)
    lastname = Column(String(20), nullable=False)
    subscription_date = Column(Date)



class Address(Base):
    __tablename__ = 'address'
   
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

    def to_dict(self):
        return {}

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String (100), nullable=False)
    description = Column(String (100), nullable=False)
    height = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    gender = Column(String)
    homeworld = Column(String)
    birth_year = Column(String)

class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    diameter = Column(String)
    rotation_period = Column(String)
    orbital_period = Column(String)
    gravity = Column(String)
    population = Column(String)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(String)
    url = Column(String)

class FavoriteCharacters(Base):  #Muchos a Muchos
    __tablename__='favorite_character'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))

    users = relationship(Users)
    characters = relationship(Characters)

class FavoritePlanets(Base):  # Muchos a muchos
    __tablename__='favorite_planets'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))

    users = relationship(Users)
    planets = relationship(Planets)

class Profiles(Base):
    __tablename__='profiles'
    id = Column(Integer,primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    nickname = Column(String)
    image_url = Column(String)
    users_id = Column(Integer, ForeignKey('users.id'), unique=True)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
