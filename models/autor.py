from sqlalchemy import *
from sqlalchemy.orm import relationship


from models.base import Base



class Autor(Base):
    __tablename__ = 'ib_autor'
    id =  Column(Integer, primary_key=True)
    nombre = Column (String (30))
    