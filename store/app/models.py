from sqlalchemy import Column,Integer,String
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Kids(Base):
    __tablename__ = 'KIDS_STORE'

    id = Column(Integer, primary_key=True, nullable=False)
    catagory=Column(String, nullable=False) 
    company_name=Column(String,nullable=False)
    color=Column(String, nullable=False)

class Users(Base):
    __tablename__ = "USERS"

    user_id = Column(Integer,nullable=False,primary_key=True)
    user_name = Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)
   
class Mens(Base):
    __tablename__ = 'MENS_STORE'

    id = Column(Integer, primary_key=True, nullable=False)
    dress_type=Column(String, nullable=False) 
    company_name=Column(String,nullable=False)
    color=Column(String, nullable=False)

class Womens(Base):
    __tablename__ = 'WOMENS_STORE'

    id = Column(Integer, primary_key=True, nullable=False)
    dress_type=Column(String, nullable=False) 
    company_name=Column(String,nullable=False)
    color=Column(String, nullable=False)


