from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER as Integer
from sqlalchemy.dialects.postgresql import TEXT as Text
from app.database import BASE

class User(BASE):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)

    def __init__(self, name: str):
        self.name = name