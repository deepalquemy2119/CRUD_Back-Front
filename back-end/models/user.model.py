from sqlalchemy import Column, String, Integer

from database import CustomToDo

class User(CustomToDo):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), index=True, unique=True)
    email = Column(String(45), index=True, unique=True)
    password = Column(String(30), index=True)

