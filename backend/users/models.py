import os
import secrets
import shutil
from typing import List, Optional
import aiofiles
from bson import ObjectId
from fastapi import File, HTTPException, Request, Security, status, UploadFile
from db import db
from datetime import datetime
import bcrypt
from pydantic import EmailStr
from auth.jwt_handler import jwt_dependecy, sign_jwt
import uuid
from fastapi.encoders import jsonable_encoder
from posts.models import  allowed_file, get_post_by_user_id, save_images
from werkzeug.utils import secure_filename

from users.schemas import User, UserLogin, UserOut, UserUpdate 

UPLOAD_FOLDER = 'static/profile_pic/'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


def encrypt_password(password: str):
    print("password:", password)
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

def compare_passwords(pass_1:str, pass_2:str):
    print("pass_1:", pass_1)
    print("pass_2:", pass_2)
    # print(pass_1, pass_2)
    encode_pass_1 = pass_1.encode()
    encode_pass_2 = pass_2.encode()
    print("encode_pass_1:", encode_pass_1)
    print("encode_pass_2:", encode_pass_2)
    print("bcrypt.checkpw(encode_pass_1, encode_pass_2):", bcrypt.checkpw(encode_pass_1, encode_pass_2))
    return bcrypt.checkpw(pass_1.encode(), pass_2.encode())


async def save_profile_picture(images: Optional[UploadFile] = None):
    saved_images = []
    if images:
        if allowed_file(images.filename):
            images.filename = secure_filename(images.filename)
            images.filename = secrets.token_hex(8) + images.filename
            image_path = os.path.join(UPLOAD_FOLDER, images.filename)
            image_url = f"http://localhost:8000/{image_path}"
            print(image_url)
            async with aiofiles.open(image_path, 'wb') as buffer:
                content = await images.read()
                # print(content)
                await buffer.write(content)
                images.filename = image_url
            saved_images.append(images.filename)
        else:
            raise HTTPException(status_code=400, detail="Invalid image format")
    return saved_images


async def create_user(username: str, email: str,  password: str, confirm_password:str,  bio: str, profile_pic_url: Optional[UploadFile] = None):
    user = User( 
        username=username,
        email=email,
        password=password,
        confirm_password=confirm_password,
        bio=bio,
        profile_pic_url=profile_pic_url,
    )
    
    user_dict = user.user_dict()
    
    '''make the profile_pic_url an optional field and set a default value if it is empty'''
    if user_dict['profile_pic_url'] == None:
        user_dict['profile_pic_url'] = ['https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png']
    else:
        user_dict['profile_pic_url'] = await save_profile_picture(user_dict['profile_pic_url'])
    print("user_password:", user_dict['password'])
    user_dict['password'] = encrypt_password(user_dict['password']) 
    user_dict['updated_at'] = datetime.now()
    
    '''check if the user already exists'''
    if db.users.find_one({"email": user_dict['email']}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    '''confirm password match'''
    user.confirm_passwords_match()
    user = db.users.insert_one(user_dict)
    user = db.users.find_one({"_id": user.inserted_id})
    user["_id"] = str(user["_id"])
    
    return user


def get_all_users():
    users = db.users.find({})
    all_users = []
    for user in users:
        user = UserOut(**user)
        user.profile_pic_url =[str(url) for url in user.profile_pic_url] if user.profile_pic_url else None
        user = user.dict()
        all_users.append(user)
    return all_users

def user_login(user_login: UserLogin):
    email = user_login.email
    password = user_login.password
    user = db.users.find_one({"email": email})
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    print(user["password"])
    if not compare_passwords(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials"
        )
    user["_id"] = str(user["_id"])
    owner = user['_id']
    posts = get_post_by_user_id(owner)
    user = UserOut(**user).dict()
    user["posts"] = posts
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

def update_user_by_id(user_id: str, updated_user: UserUpdate):
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
    # if profile_pic:
    #     updated_user["profile_pic_url"] = save_profile_picture(profile_pic)
    updated_user["updated"] = str(datetime.now())
    user = db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": updated_user}
    )
    user = db.users.find_one({"_id": ObjectId(user_id)})
    user["_id"] = str(user["_id"])
    return user



   
    
   




    

