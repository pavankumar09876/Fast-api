from sqlalchemy import Integer, String, Column, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class user1(Base):
    __tablename__='users'

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String, unique=True)
    password=Column(String)

    blogs=relationship("Blog",back_populates='author')

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    context = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    author=relationship("user1", back_populates="blogs")

