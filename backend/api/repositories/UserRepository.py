from database import db

from models.UserModel import User
from schemas.UserSchema import UserCreate, UserResponse 


# CRUD

# C CREATE
async def create(request_body: UserCreate):
    new_user = User(email=request_body.email, name=request_body.name)
    db.add(new_user)
    await db.commit()
    db.refresh(new_user)

    return new_user

# R READ


# U UPDATE


# D DELETE