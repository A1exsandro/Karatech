from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
