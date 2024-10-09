from fastapi import Depends, APIRouter, HTTPException

from repositories import UserRepository
from schemas.UserSchema import UserCreate, UserResponse


router = APIRouter(
    prefix="/user",
    tags=['Usuários']
)


# CREATE
@router.post("", response_model=UserResponse)
async def create(create_form: UserCreate):
    return await UserRepository.create(create_form)
