from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

# Pydantic schema for creating a new user
class UserCreate(UserBase):
    pass

# Pydantic schema for returning a user with an ID
class User(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True  # Change from orm_mode to from_attributes

