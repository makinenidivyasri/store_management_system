from typing import List
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app import schemas
from app import database,models
from app.database import get_db
from random import randrange
from passlib.context import CryptContext
from .. import utils

password_context = CryptContext(schemes=["bcrypt"] , deprecated = "auto")

router = APIRouter(tags = ['Users'])

@router.get("/users",response_model=List[schemas.UserOutput])
def user_create(db: Session=Depends(get_db)):
    users = db.query(models.Users).all()
    print(users)
    return users

@router.post("/users/createuser",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOutput)
def user_create(user : schemas.NewUser,db:Session=Depends(get_db)):
    user.user_id = randrange(11111,99999)  
    user.password = utils.hash(user.password)
    users = models.Users(**user.model_dump())
    db.add(users)
    db.commit()
    db.refresh(users)
    return users

@router.get("/users/getUserByID/{id}",status_code=status.HTTP_200_OK,response_model=schemas.UserOutput)
def get_user_by_id(id : int,db:Session=Depends(get_db)):
    details = db.query(models.Users).filter(models.Users.user_id == id).first()
    if details == None:
        print(f'{id} does not exist')
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return details






