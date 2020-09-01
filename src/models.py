import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(50))
    profile = Column(String())
    emisor = relationship("Message", backref="author") 
    receptor = relationship("Message", backref="author") 
    follower = relationship("Invitations", backref="author") 
    following = relationship("Invitations", backref="author") 

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    accepted = Column(Boolean())
    date = Column(DateTime, nullable=False)
    emisor_id = Column(Integer, ForeignKey('user.id'))
    receptor_id = Column(Integer, ForeignKey('user.id'))

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    photo = Column(String())
    effects = Column(String())
    message_id = Column(Integer, ForeignKey('message.id'))
    message = relationship(Message)        
 
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    photo = Column(String()) 
    effects = Column(String())
    description = Column(String())
    username_id = Column(Integer, ForeignKey('user.id'))
    username = relationship(User) 

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comments = Column(String())
    date = Column(DateTime, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    like = Column(String())
    date = Column(DateTime, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
   
class Invitations(Base):
    __tablename__ = 'invitations'
    id = Column(Integer, primary_key=True)
    accepted = Column(Boolean())
    create_at = Column(DateTime())
    answered_at = Column(DateTime())
    follower_id = Column(Integer, ForeignKey('user.id'))
    followed_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')



# ------------------  Importanteeee para que funcione ------------
# 1 chequear que version tiene $ python3 --version //// el dira cual tiene
# 2 ir al archivo Pipfile y cambiar python_version por la version q dijo 
# 3 $ pipenv install
# 4 $ pipenv shell
# 5 ahora vas cambiando el codigo en models.py y cuando lo guarde se pone esto
# 6 $ python src/models.py
# 7 en diagram.png va a ir cambiando
# 8 para volver a actualizar ir de paso 5 a paso 7