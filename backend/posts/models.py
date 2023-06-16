import json
import secrets
import shutil
from typing import List, Optional
import aiofiles
from bson import ObjectId
from fastapi import Depends, FastAPI, HTTPException, status, UploadFile, File
from auth.jwt_handler import get_current_user, jwt_dependecy
from db import db
from datetime import datetime
import bcrypt
from pydantic import EmailStr
import uuid
from bson.binary import Binary
from werkzeug.utils import secure_filename
import os
from PIL import Image
from fastapi.staticfiles import StaticFiles

from posts.schemas import Post
from gridfs import GridFS

fs = GridFS(db)

app= FastAPI()


UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

'''give access to static files'''
app.mount("/static", StaticFiles(directory=UPLOAD_FOLDER), name="static")


def get_current_user_id( user: dict = Depends(get_current_user)):
    return user

def allowed_file(filename: str) -> bool:
    filename = filename.lower()
    filename = filename.replace(' ', '_')
    filename = secure_filename(filename)
    filename = str(uuid.uuid4()) + filename
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

async def save_images(images: List[UploadFile]):
    saved_images = []
    for image in images:
        if allowed_file(image.filename):
            image.filename = secure_filename(image.filename)
            image.filename = secrets.token_hex(10) + image.filename
            print('image.filename', image.filename)
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            print('image_path', image_path)
            image_url = f"http://localhost:8000/{image_path}"
            print('image_url', image_url)
            file_content = await image.read()
            with open(image_path, 'wb') as f:
                f.write(file_content)
            image.filename = image_url
            saved_images.append(image.filename)
            print('saved_images', saved_images)
        else:
            raise HTTPException(status_code=400, detail="Invalid image format")
    return saved_images
    #         async with aiofiles.open(image_path, 'wb') as buffer:
    #             content = await image.read()  # async read
    #             await buffer.write(content)  # async write
    #         saved_images.append(image.filename)
    #     else:
    #         raise HTTPException(status_code=400, detail="Invalid image format")
    # return saved_images

def get_all_posts():
    posts = db.posts.find({})
    posts = [Post(**post) for post in posts]
    return posts

def get_post_by_id(post_id: str):
    post = db.posts.find_one({"post_id": post_id})
    owner = get_post_owner(post_id)
    print('owner', owner)
    if post:
        return Post(**post)
    else:
        raise HTTPException(status_code=404, detail="Post not found")
    
def get_post_by_user_id(user_id: str):
    posts = db.posts.find({"owner": user_id})
    posts = [Post(**post) for post in posts]
    return posts

def get_post_owner(post_id: str):
    post = db.posts.find_one({"post_id": post_id})
    if post:
        return post['owner']
    else:
        raise HTTPException(status_code=404, detail="Post not found")

def delete_post_by_id(post_id: str):
    post = db.posts.find_one({"post_id": post_id})
    if post:
        db.posts.delete_one({"post_id": post_id})
        return True
    else:
        raise HTTPException(status_code=404, detail="Post not found")
    
def update_post_by_id(post_id: str, title: str, content: str, images: Optional[List[str]] = None):
    post = db.posts.find_one({"post_id": post_id})
    db_images = post['images']
    print('images', db_images)
    for image in images:
        db_images.append(image)
    print('db_images', db_images)
    if post:
        db.posts.update_one({"post_id": post_id}, {"$set": {"title": title, "content": content, "images": db_images}})
        return {"message": "Post has been updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

    

