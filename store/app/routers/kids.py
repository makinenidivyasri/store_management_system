from typing import List
from fastapi import status , HTTPException, Depends, APIRouter
from app import schemas,models
from random import randrange
from app.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from .. import oauth2

router = APIRouter(tags = ['Kids'])

@router.get("/kids",status_code=status.HTTP_200_OK,response_model=List[schemas.Kids])
def get_kids_acceessries(db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    details = db.query(models.Kids).all()
    print(details) 
    return details

@router.post("/kids/addKidsWear/",status_code=status.HTTP_201_CREATED,response_model=schemas.Kids)
def add_item_in_kids(item : schemas.NewKidsWear,db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    item.id = randrange(1000,9999)
    added_item= models.Kids(**item.model_dump())
    if added_item == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    db.add(added_item)
    db.commit()
    db.refresh(added_item)
    print(added_item) 
    return added_item

@router.put("/kids/modifyKidsWearData/{id}",status_code=status.HTTP_200_OK,response_model=schemas.ModifyKidsWearOutput)
async def modify_kids_wear_data(id : int,modify_data : schemas.ModifyKidsWear,db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    data_query = db.query(models.Kids).filter(models.Kids.id==id) 
    if not (data_query.first()):
        print(f'id: {id} does not exist')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    print(type(data_query.first()))
    data_query.update(modify_data.model_dump(),synchronize_session=False) 
    db.commit()
    data = data_query.first()
    return data

@router.delete("/kids/deleteKidsWearItem/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_kids_wear_item(id : int,db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    details = db.query(models.Kids).filter(models.Kids.id == id)
    to_be_deleted_item = details.first()
    if to_be_deleted_item == None:
        print("id does not exist")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    details.delete()
    print("item deleted")
    db.commit()
    return {f'ID : {id} is deleted'}

@router.get("/kids/getKidsDataByID/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Kids)
def get_kids_wear_data_by_id(id : int,db:Session=Depends(get_db),access = Depends(oauth2.get_current_user)):
    details = db.query(models.Kids).filter(models.Kids.id == id).first()
    if details == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return details

