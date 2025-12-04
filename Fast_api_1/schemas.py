from pydantic import BaseModel, Field, ConfigDict

class blog(BaseModel):
    title: str 
    context: str
    user_id: int

class BlogResponse(BaseModel):
    id: int
    title: str
    context: str
    user_id: int

    model_config={
        'from_attributes': True
    }

class usercreate(BaseModel):
    name:str
    email:str
    password:str=Field(max_length=72)

class showuser1(BaseModel):
    name:str
    email:str

    blogs:list[BlogResponse]=[]

    model_config={
        'from_attributes':True
    }

class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
