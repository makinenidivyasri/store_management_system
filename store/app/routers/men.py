from typing import List
from fastapi import status , HTTPException, Depends, APIRouter
from app import schemas,models
from random import randrange
from app.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from .. import oauth2

router = APIRouter(tags = ['Men'])

@router.get("/mens",status_code=status.HTTP_200_OK,response_model=List[schemas.Mens])
def get_men_acceessries(db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    details = db.query(models.Mens).all()
    print(details) 
    return details

@router.post("/mens/addMensWear/",status_code=status.HTTP_201_CREATED,response_model=schemas.Mens)
def add_item_in_men(item : schemas.NewMensWear,db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    item.id = randrange(1000,9999)
    added_item= models.Mens(**item.model_dump())
    if added_item == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    db.add(added_item)
    db.commit()
    db.refresh(added_item)
    print(added_item)
    return added_item

@router.put("/mens/modifyMensWearData/{id}",status_code=status.HTTP_200_OK,response_model=schemas.ModifyMensWearOutput)
async def modify_men_wear_data(id : int,modify_data : schemas.ModifyMensWearData,db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    data_query = db.query(models.Mens).filter(models.Mens.id==id) 
    if not (data_query.first()):
        print(f'id: {id} does not exist')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    print(type(data_query.first()))
    data_query.update(modify_data.model_dump(),synchronize_session=False) 
    db.commit()
    data = data_query.first() 
    return data

@router.delete("/mens/deleteMensWearItem/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_men_wear_item(id : int,db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    details = db.query(models.Mens).filter(models.Mens.id == id)
    to_be_deleted_item = details.first()
    if to_be_deleted_item == None:
        print("id does not exist")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    details.delete()
    print("item deleted")
    db.commit()
    return {f'ID : {id} is deleted'}

@router.get("/mens/getMensDataByID/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Mens)
def get_men_wear_data_by_id(id : int,db:Session=Depends(get_db),access = Depends(oauth2.get_current_user)):
    details = db.query(models.Mens).filter(models.Mens.id == id).first()
    if details == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return details

