#all authentication path operations are here
from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, oauth2,schemas,models
from .. import utils,oauth2

router = APIRouter(tags = ['Authentication'])

@router.get("/login")
def user_login(users_credentials : OAuth2PasswordRequestForm = Depends() ,db:Session=Depends(database.get_db)):
    user_details = db.query(models.Users).filter(models.Users.user_name == users_credentials.username).first()
    print(user_details)
    if user_details == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")
    if not utils.verify_password(users_credentials.password,user_details.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")
    access_token = oauth2.create_access_token(data= {"user_id": user_details.user_id})

    return {"token": access_token,"Token_type": "bearer"}





