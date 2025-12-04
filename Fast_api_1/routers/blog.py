from fastapi import APIRouter, Depends, HTTPException,status
from .. import schemas, models,database
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog
from ..oauth2 import get_current_user 

router=APIRouter(
    prefix='/blogs',
    tags=['Blogs'],
    dependencies=[Depends(get_current_user)]
)
get_db=database.get_db


@router.get('/', response_model=List[schemas.BlogResponse])
def All_blogs(db:Session=Depends(get_db)):
    return blog.get_all(db)
   

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.BlogResponse)
def create(request:schemas.blog,db:Session=Depends(get_db)):
    return blog.create(request,db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.BlogResponse)
def single_value(id:int, db:Session=Depends(get_db)):
    return blog.get_singleblog(id,db)


@router.put('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.BlogResponse)
def update(id:int,request:schemas.blog,db:Session=Depends(get_db)):
    return blog.update(id,db,request)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session=Depends(get_db)):
    return blog.destroy(id,db)