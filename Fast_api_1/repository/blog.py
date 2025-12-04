from fastapi import HTTPException,status
from .. import models,schemas
from sqlalchemy.orm import Session


def get_all(db:Session):
    blog=db.query(models.Blog).all()
    return blog


def create(request:schemas.blog,db:Session):
    user = db.query(models.user1).filter(models.user1.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {request.user_id} not found")
    
    new_blog = models.Blog(
        title=request.title,
        context=request.context,
        user_id=request.user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_singleblog(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return blog


def update(id:int,db:Session,request:schemas.blog):
    blog_query=db.query(models.Blog).filter(models.Blog.id==id)
    blog=blog_query.first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} is not available or entered correct values")
    blog_query.update(request.model_dump(), synchronize_session=False)
    db.commit()
    return blog_query.first()


def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Delete {id} is successful"}