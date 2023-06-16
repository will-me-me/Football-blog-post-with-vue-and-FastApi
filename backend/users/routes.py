from typing import List, Optional
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi import FastAPI
import users.models as user_models
from db import db

from users.schemas import User, UserOut

router = APIRouter()

@router.post("/login")
def user_login(user_login: user_models.UserLogin):
    return user_models.user_login(user_login)


@router.post("/create-user")
async def create_user(
    username: str,
    email: str,
    password: str,
    confirm_password: str,
    bio : str,
    profile_pic_url:  Optional[UploadFile] = File(None) 
):
    return await user_models.create_user(username, email, password, confirm_password, bio, profile_pic_url)

    


@router.post("/update_user", response_model=UserOut)
def update_user_by_id(user_id: str, updated_user: user_models.UserUpdate):
    return user_models.update_user_by_id(user_id, updated_user)

@router.get("/get_all_users")
def get_all_users():
    return user_models.get_all_users()
    
