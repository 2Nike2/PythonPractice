from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import INTEGER as Integer
from sqlalchemy.dialects.postgresql import TEXT as Text
from sqlalchemy.dialects.postgresql import BOOLEAN as Boolean
from sqlalchemy.dialects.postgresql import TIMESTAMP as TimeStamp
from sqlalchemy.orm import relationship
from app.database import BASE
from datetime import datetime as dt

class Todo(BASE):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(Text)
    description = Column(Text)
    finished = Column(Boolean)
    deadline = Column(TimeStamp)

    users = relationship("User")

    def __init__(self, user_id: int, title: str, description: str, deadline: dt):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.finished = False
        self.deadline = deadline