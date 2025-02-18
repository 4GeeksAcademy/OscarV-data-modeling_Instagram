import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

#python src/models.py

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname= Column(String(250), nullable=False)
    email= Column(String(250), nullable=False)
    
class Post(Base):
    __tablename__ = 'post'
    id_post = Column(Integer, primary_key=True)
    url_media = Column(String(250))
    descripcion = Column(String(250))
    like =Column(Integer)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    id_com = Column(Integer, primary_key=True)
    comments = Column(String(250))
    id_post = Column(Integer, ForeignKey('post.id_post'))
    post = relationship(Post)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Followers(Base):
    __tablename__ = 'followers'
    id_foll = Column(Integer, primary_key=True)
    date = Column(DateTime)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    id_follow = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
