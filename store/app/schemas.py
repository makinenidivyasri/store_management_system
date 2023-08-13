from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from typing import Optional
import email_validator
from pydantic import EmailStr
from datetime import datetime

#response models for kids
class NewKidsWear(BaseModel):
    id : Optional[int] = None
    catagory : str  #girls/boys 
    company_name : str
    color : str

class Kids(NewKidsWear):
    #all attritutes will be inherited from parent class.
    class Config:
        from_attributes = True

class ModifyKidsWear(BaseModel):
    catagory : Optional[str] = None 
    company_name : Optional[str] = None
    color : Optional[str] = None

class ModifyKidsWearOutput(ModifyKidsWear):
    id : int
    class Config:
        from_attributes = True

#response models for users
class NewUser(BaseModel):
    user_id : Optional[int] = None
    user_name : EmailStr
    password : str 

class UserOutput(BaseModel):
    user_id : int
    user_name : EmailStr
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    user_name : EmailStr
    password : str 

#response models for token
class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None

#response models for men
class NewMensWear(BaseModel):
    id : Optional[int] = None
    dress_type : str  
    company_name : str
    color : str

class Mens(NewMensWear):
    #all attritutes will be inherited from parent class.
    class Config:
        from_attributes = True

class ModifyMensWearData(BaseModel):
    dress_type : Optional[str] = None 
    company_name : Optional[str] = None
    color : Optional[str] = None

class ModifyMensWearOutput(ModifyMensWearData):
    id : int
    class Config:
        from_attributes = True

#response models for women 
class NewWomensWear(BaseModel):
    id : Optional[int] = None
    dress_type : str  
    company_name : str
    color : str

class Womens(NewWomensWear):
    #all attritutes will be inherited from parent class.
    class Config:
        from_attributes = True

class ModifyWomensWearData(BaseModel):
    dress_type : Optional[str] = None 
    company_name : Optional[str] = None
    color : Optional[str] = None

class ModifyWomensWearOutput(ModifyWomensWearData):
    id : int
    class Config:
        from_attributes = True