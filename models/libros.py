from sqlalchemy import *
from sqlalchemy.orm import relationship


from models.base import Base



class Libro(Base):
    __tablename__ = 'ib_libro'
    id =  Column(Integer, primary_key=True)
    titulo = Column (String (300))
    autor = Column (String (300))  
    año = Column (Integer)
    editorial = Column (String (300))
    unidades = Column (Integer) 
    ubicacion = Column (String (100))  

