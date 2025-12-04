from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from .database import get_db
from . import models
from .token import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = db.query(models.user1).filter(models.user1.name == username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user
