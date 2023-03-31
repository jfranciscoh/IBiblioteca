from sqlalchemy import *
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash

from models.base import Base



class Usuario(Base):
    __tablename__ = 'voc_usuario'
    id =  Column(Integer, primary_key=True)
    username = Column (String (100))
    password = Column (String (512))  

def create_user(username:str, clear_password:str) -> Usuario:
	user = Usuario()
	user.username = username
	user.password = generate_password_hash(clear_password)

	return user