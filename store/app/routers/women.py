from typing import List
from fastapi import status , HTTPException, Depends, APIRouter
from app import schemas,models
from random import randrange
from app.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from .. import oauth2

router = APIRouter(tags = ['Women'])

@router.get("/womens",status_code=status.HTTP_200_OK,response_model=List[schemas.Womens])
def get_Women_acceessries(db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    details = db.query(models.Womens).all()
    print(details) 
    return details

@router.post("/womens/addWomensWear/",status_code=status.HTTP_201_CREATED,response_model=schemas.Womens)
def add_item_in_Women(item : schemas.NewWomensWear,db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    item.id = randrange(1000,9999)
    added_item= models.Womens(**item.model_dump())
    if added_item == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    db.add(added_item)
    db.commit()
    db.refresh(added_item)
    print(added_item)
    return added_item

@router.put("/womens/modifyWomensWearData/{id}",status_code=status.HTTP_200_OK,response_model=schemas.ModifyWomensWearOutput)
async def modify_Women_wear_data(id : int,modify_data : schemas.ModifyWomensWearData,db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    data_query = db.query(models.Womens).filter(models.Womens.id==id) 
    if not (data_query.first()):
        print(f'id: {id} does not exist')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    print(type(data_query.first()))
    data_query.update(modify_data.model_dump(),synchronize_session=False) 
    db.commit()
    data = data_query.first() 
    return data

@router.delete("/womens/deleteWomensWearItem/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_Women_wear_item(id : int,db: Session = Depends(get_db),access = Depends(oauth2.get_current_user)):
    details = db.query(models.Womens).filter(models.Womens.id == id)
    to_be_deleted_item = details.first()
    if to_be_deleted_item == None:
        print("id does not exist")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    details.delete()
    print("item deleted")
    db.commit()
    return {f'ID : {id} is deleted'}

@router.get("/womens/getWomensDataByID/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Womens)
def get_Women_wear_data_by_id(id : int,db:Session=Depends(get_db),access = Depends(oauth2.get_current_user)):
    details = db.query(models.Womens).filter(models.Womens.id == id).first()
    if details == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return details

