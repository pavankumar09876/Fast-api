from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,models,database
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user
from typing import List

router=APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db=database.get_db


@router.get('/', response_model=List[schemas.showuser1])
def get_allusers(db:Session=Depends(get_db)):
    return user.all_users(db)

@router.post('/', response_model=schemas.showuser1)
def create_user(request:schemas.usercreate,db:Session=Depends(get_db)):
   return user.create_user(request,db)

@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.showuser1)
def get_user(id:int,db:Session=Depends(get_db)):
    return user.get_singleuser(id,db)