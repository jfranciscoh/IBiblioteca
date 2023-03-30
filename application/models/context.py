from sqlalchemy import create_engine, Sequence, event
from sqlalchemy.orm import sessionmaker, Session
from app.models.base import  Base

from app.instance.config import SQL_ALCHEMY_DATABASE_URI, SQL_ALCHEMY_DATABASE_OPTION

Session = sessionmaker()

def init_db():
	""" Inicia el factory Session con los parametros necesarios para conectarnos a nuestra base de datos"""
	engine = create_engine(SQL_ALCHEMY_DATABASE_URI, pool_size=50)
	Session.configure(bind=engine)
	engine.connect()

def create_production_database():
	""" Crea la base de datos (DROP/CREATE) """
	print("* /_!_\ Inicializacion de base de datos")
	print("* Ubicacion: " + str(SQL_ALCHEMY_DATABASE_URI) + " opcion: " + str(SQL_ALCHEMY_DATABASE_OPTION))

	""" Establish first connection """
	engine = create_engine(SQL_ALCHEMY_DATABASE_URI, pool_size=50)
	Session.configure(bind=engine)
	engine.connect()
	continue_value = input("Este procedimiento va a borrar TODOS los datos de la base mencionada y volver a crearla, seguro desea seguir ? (s/n)")

	if continue_value == 's':
		with Session() as session:
			print(" * [SA] /_!_\ DROPPING DATABASE")
			Base.metadata.drop_all(engine)
			print(" * [SA] /_!_\ CREATING DATABASE")
			Base.metadata.create_all(engine)
			print(" * [SA] Database created succesfully")
			session.commit()
		print(" * [SA] Dialect : " + str(engine.url.get_dialect().name))