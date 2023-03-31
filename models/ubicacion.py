from sqlalchemy import *
from sqlalchemy.orm import relationship


from models.base import Base



class Ubicacion(Base):
    __tablename__ = 'ib_ubicacion'
    id =  Column(Integer, primary_key=True)
    nombre = Column (String (30))
    