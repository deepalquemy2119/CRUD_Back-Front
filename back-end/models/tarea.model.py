from sqlalchemy import Column, String, Integer

from database import CustomToDo

class Tarea(CustomToDo):
    __tablename__ = 'tareas'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), index=True, unique=True)
    description = Column(String(255), index=True, cascade=all)
    state = Column(bool, index=True)
    date = Column(date)
    mailid = Column(int, ForeignKey('user.email'))


