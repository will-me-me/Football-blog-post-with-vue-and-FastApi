import shutil
from bson import ObjectId
from fastapi import HTTPException, status, UploadFile
from db import db
from datetime import datetime
import bcrypt
from pydantic import EmailStr
import uuid

from users.schemas import User 


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
    users = list(db.users.find({}))
    for user in users:
        user["_id"] = str(user["_id"])
    return users
    



   
    
   




    

