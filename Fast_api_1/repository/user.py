from fastapi import HTTPException,status
from .. import models,schemas,database
from sqlalchemy.orm import Session
from ..hashing import Hash


def all_users(db:Session):
    users=db.query(models.user1).all()
    return users

def create_user(request: schemas.usercreate, db: Session):
    # hashed_pwd=hash_password(request.password)
    new_user = models.user1(name=request.name,
                            email=request.email,
                            password=Hash.hash_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_singleuser(id:int,db:Session):
    user=db.query(models.user1).filter(models.user1.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{id} is not available')
    return user