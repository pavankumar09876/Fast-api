from fastapi import FastAPI,Depends, status,Response,HTTPException
from . import schemas,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED, response_model=schemas.SecondBlog)

def create(request:schemas.Blog, 
           db: Session=Depends(get_db)):
    new_blog=models.Blog(name=request.name,
                         rollno=request.rollno,
                         rank=request.rank,
                         password=request.password)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def all_blogs(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs


@app.get('/blogs', status_code=status.HTTP_200_OK)
def single_blog(id,response: Response,db:Session=Depends(get_db)):
    single_blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not single_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Not available in db this {id}')
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'details':f'Not available in db this {id}'}
    return single_blog


@app.put('/blogs/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
    blog_query=db.query(models.Blog).filter(models.Blog.id==id)
    blog=blog_query.first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Not available in db this {id}')
    blog_query.update(request.dict(),synchronize_session=False  )
    db.commit()
    return {"message": "updated"}


@app.delete('/blogs{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Not available in db this {id}')
    blog.delete(synchronize_session=False)
    db.commit()
    return f"Delete {id} is successfully"