from jose import jwt,JWTError
from datetime import datetime,timedelta
from . import schemas,database,models
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException,status
from sqlalchemy.orm import Session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "/login") 

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TIME_EXPIRE_MINUTES = 60

def create_access_token(data : dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes= ACCESS_TIME_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token : str,credentials_exceptions):
    try:
        payload = jwt.decode(token , SECRET_KEY,algorithms=ALGORITHM)
        id : str = payload.get("user_id")
        if id == None:
            raise credentials_exceptions
        token_data = schemas.TokenData(id = id)
    except JWTError:
        raise credentials_exceptions
    return token_data

def get_current_user(token : str = Depends(oauth2_scheme),db:Session =Depends(database.get_db)):
    credentials_exceptions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f'could not validate credentials',headers={"WWW-Authenticate": "Bearer"})
    
    return verify_access_token(token, credentials_exceptions)