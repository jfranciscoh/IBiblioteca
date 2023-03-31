from sqlalchemy import create_engine, Sequence, event
from sqlalchemy.orm import sessionmaker, Session
from models.base import  Base
from instance.config import SQL_ALCHEMY_DATABASE_URI

Session = sessionmaker()

def init_db():
	""" Production database """
	""" Create all tables """
	engine = create_engine(SQL_ALCHEMY_DATABASE_URI, pool_size=50)
	Session.configure(bind=engine)
	""" Establish first connection """
	engine.connect()