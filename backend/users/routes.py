from fastapi import APIRouter
from fastapi import FastAPI
import users.models as user_models

from users.schemas import UserOut

router = APIRouter()

@router.post("/login", response_model=UserOut)
def user_login(user_login: user_models.UserLogin):
    return user_models.user_login(user_login)

@router.post("/create_user", response_model=UserOut)
def create_user(new_user: user_models.User):
    return  user_models.create_user(new_user)

@router.post("/update_user", response_model=UserOut)
def update_user_by_id(user_id: str, updated_user: user_models.User):
    return user_models.update_user_by_id(user_id, updated_user)

@router.get("/get_all_users")
def get_all_users():
    return user_models.get_all_users()
    
