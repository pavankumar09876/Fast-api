from pydantic import BaseModel


class Blog(BaseModel):
    name: str
    rollno: int
    rank: int
    password:str

class SecondBlog(BaseModel):
    name: str
    rollno: int
    rank: int

    class Config:
        orm_mode = True