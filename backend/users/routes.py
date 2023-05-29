from fastapi import APIRouter
from fastapi import FastAPI
import users.models as user_models

from users.schemas import UserOut

router = APIRouter()

@router.post("/create_user", response_model=UserOut)
async def create_user(new_user: user_models.User):
    return await user_models.create_user(new_user)
    
