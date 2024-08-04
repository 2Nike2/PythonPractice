from dotenv import load_dotenv
load_dotenv()

import os
from contextlib import contextmanager
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_DATABASENAME = os.getenv("DB_DATABASENAME")

connection_string = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASENAME}"

ENGINE = create_engine(connection_string)

SESSION = scoped_session(sessionmaker(bind=ENGINE, autocommit=False, autoflush=False, expire_on_commit=False))

class SelfBase(object):
    def to_dict(self):
        model = {}
        for column in self.__table__.columns:
            model[column.name] = str(getattr(self, column.name))
        return model
    
BASE = declarative_base(cls=SelfBase)
BASE.query = SESSION.query_property()

@contextmanager
def session_scope():
    session = SESSION()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()