from sqlalchemy import create_engine, Sequence, event
from sqlalchemy.orm import sessionmaker, Session
from models.base import  Base
from instance.config import SQL_ALCHEMY_DATABASE_URI
from libros import Libro
from ubicacion import Ubicacion
from usuario import Usuario


Session = sessionmaker()


def init_db():

	engine = create_engine(SQL_ALCHEMY_DATABASE_URI, pool_size=50)
	Session.configure(bind=engine)
	engine.connect()