from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Login']
)
get_db = database.get_db


@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.user1).filter(models.user1.name == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if not Hash.verify(user.password, form_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect Password')

    access_token = token.create_access_token(data={"sub": user.name})
    return {"access_token": access_token, "token_type": "bearer"}
