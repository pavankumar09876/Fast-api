from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL='postgresql://postgres:6585@localhost:5432/fast_api'

engine=create_engine(DATABASE_URL)

sessionlocal=sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base= declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()