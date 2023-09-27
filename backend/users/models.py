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
from posts.models import allowed_file, get_post_by_user_id
from werkzeug.utils import secure_filename
from fastapi import UploadFile
from users.schemas import User, UserLogin, UserOut, UserUpdate

UPLOAD_FOLDER = "static/profile_pic/"
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]


def encrypt_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def compare_passwords(pass_1: str, pass_2: str):
    return bcrypt.checkpw(pass_1.encode(), pass_2.encode())


async def save_profile_picture(images: Optional[UploadFile] = None):
    saved_images = []
    if images:
        if allowed_file(images.filename):
            images.filename = secure_filename(images.filename)
            images.filename = secrets.token_hex(8) + images.filename
            image_path = os.path.join(UPLOAD_FOLDER, images.filename)
            image_url = image_path
            absolute_path = os.path.abspath(image_path)
            print("absolute_path:", absolute_path)
            print(image_url)
            image_url = absolute_path
            async with aiofiles.open(image_path, "wb") as buffer:
                content = await images.read()
                # print(content)
                await buffer.write(content)
                images.filename = image_url
            saved_images.append(images.filename)
        else:
            raise HTTPException(status_code=400, detail="Invalid image format")
    return saved_images


def confirm_pass_match(password: str, confirm_password: str):
    return password == confirm_password


async def create_user(
    username: str,
    email: str,
    password: str,
    confirm_password: str,
    bio: str,
    profile_pic_url: Optional[UploadFile] = None,
):
    user = User(
        username=username,
        email=email,
        password=password,
        confirm_password=confirm_password,
        bio=bio,
        profile_pic_url=profile_pic_url,
    )

    user_dict = user.user_dict()

    """make the profile_pic_url an optional field and set a default value if it is empty"""
    if user_dict["profile_pic_url"] is None:
        user_dict["profile_pic_url"] = [
            "https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png"
        ]
    else:
        user_dict["profile_pic_url"] = await save_profile_picture(
            user_dict["profile_pic_url"]
        )
    print("user_password:", user_dict["password"])
    user_dict["password"] = encrypt_password(user_dict["password"])
    user_dict["updated_at"] = datetime.now()

    """check if the user already exists"""
    if db.users.find_one({"email": user_dict["email"]}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )
    """confirm password match"""
    user.confirm_passwords_match()
    """save the user to the database"""
    print("user_dict:", user_dict)
    user = db.users.insert_one(user_dict)
    user = db.users.find_one({"_id": user.inserted_id})
    user["id"] = str(user["_id"])
    user.pop("_id")
    return user



def get_all_users():
    users = db.users.find({})
    all_users = []
    for user in users:
        user = UserOut(**user)
        user.profile_pic_url = (
            [str(url) for url in user.profile_pic_url] if user.profile_pic_url else None
        )
        user = user.model_dump()
        all_users.append(user)
    return all_users


def user_login(user_login: UserLogin):
    email = user_login.email
    password = user_login.password
    user = db.users.find_one({"email": email})
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    print(user["password"])
    if not compare_passwords(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials"
        )
    user["id"] = str(user["_id"])
    owner = user["id"]
    posts = get_post_by_user_id(owner)
    print(user)
    user = UserOut(**user).model_dump()
    user["posts"] = posts
    user = jsonable_encoder(user)
    token = sign_jwt(user)
    return {"token": token, "user": user}


async def get_current_user_id(request: Request, token: str = Security(jwt_dependecy)):
    user = db.users.find_one({"id": ObjectId(token)})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    user["id"] = str(user["id"])
    print(user["id"])
    return user


def update_user_by_id(user_id: str, updated_user: UserUpdate):
    user = db.users.find_one({"id": ObjectId(user_id)})
    print("user")
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    updated_user = updated_user.model_dump(exclude_unset=True)
    if "password" in updated_user:
        updated_user["password"] = encrypt_password(updated_user["password"])
    # if profile_pic:
    #     updated_user["profile_pic_url"] = save_profile_picture(profile_pic)
    updated_user["updated"] = str(datetime.now())
    user = db.users.update_one({"id": ObjectId(user_id)}, {"$set": updated_user})
    user = db.users.find_one({"id": ObjectId(user_id)})
    user["id"] = str(user["id"])
    return user
