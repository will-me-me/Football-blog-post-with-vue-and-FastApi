import shutil
from typing import Optional
from bson import ObjectId
from fastapi import HTTPException, Request, Security, status, UploadFile
from db import db
from datetime import datetime
import bcrypt
from pydantic import EmailStr
from auth.jwt_handler import jwt_dependecy, sign_jwt
import uuid
from fastapi.encoders import jsonable_encoder

from users.schemas import User, UserLogin, UserOut, UserUpdate 


def encrypt_password(password: str):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

def compare_passwords(pass_1:str, pass_2:str):
    return bcrypt.checkpw(pass_1.encode(), pass_2.encode())

def save_profile_picture(profile_pic: UploadFile):
    profile_pic_url = f"static/profile_pics/{profile_pic.filename}"
    with open(profile_pic_url, "wb") as buffer:
        shutil.copyfileobj(profile_pic.file, buffer)
    return profile_pic_url

def create_user(new_user: User, profile_pic: UploadFile = None):
    email = new_user.email
    existing_user = db.users.find_one({"email": email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    new_user.confirm_passwords_match()
    new_user.password = encrypt_password(new_user.password)
    new_user = new_user.user_dict()
    if profile_pic:
        new_user["profile_pic_url"] = save_profile_picture(profile_pic)
    db.users.insert_one(new_user)
    return new_user

    

def get_all_users():
    users = db.users.find({})
    users = [UserOut(**user).dict() for user in users]
    print(users)
    # print([user[""] for user in users])
    # for user in users:
    #     user["_id"] = str(user["_id"])
    return users

def user_login(user_login: UserLogin):
    email = user_login.email
    password = user_login.password
    user = db.users.find_one({"email": email})
    # print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    if not compare_passwords(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    user["_id"] = str(user["_id"])
    print(user['_id'])
    user = UserOut(**user).dict()
    user = jsonable_encoder(user)
    token = sign_jwt(user)
    return {"token": token, "user": user}

async def get_current_user_id(request: Request, token: str = Security(jwt_dependecy)):
    user = db.users.find_one({"_id": ObjectId(token)})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user["_id"] = str(user["_id"])
    print(user['_id'])
    return user

def update_user_by_id(user_id: str, updated_user: UserUpdate, profile_pic: UploadFile = None):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    print("user")
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    updated_user = updated_user.dict(exclude_unset=True)
    if "password" in updated_user:
        updated_user["password"] = encrypt_password(updated_user["password"])
    if profile_pic:
        updated_user["profile_pic_url"] = save_profile_picture(profile_pic)
    updated_user["updated"] = str(datetime.now())
    db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": updated_user}
    )
    return updated_user
    



   
    
   




    

