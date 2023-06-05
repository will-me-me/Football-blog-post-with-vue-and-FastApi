import json
import shutil
from typing import List
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


UPLOAD_FOLDER = './static/images/'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

'''give access to static files'''
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_current_user_id( user: dict = Depends(get_current_user)):
    return user

def allowed_file(filename: str) -> bool:
    filename = filename.lower()
    filename = filename.replace(' ', '_')
    filename = secure_filename(filename)
    filename = str(uuid.uuid4()) + filename
    print('filename', filename)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

async def save_images(images: List[UploadFile]):
    saved_images = []
    for image in images:
        if allowed_file(image.filename):
            image.filename = secure_filename(image.filename)
            image.filename = str(uuid.uuid4()) + image.filename
            print('image.filename', image.filename)
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            print('image_path', image_path)
            
            async with aiofiles.open(image_path, 'wb') as buffer:
                content = await image.read()  # async read
                await buffer.write(content)  # async write
            saved_images.append(image.filename)
        else:
            raise HTTPException(status_code=400, detail="Invalid image format")
    return saved_images

def get_all_posts():
    posts = db.posts.find({})
    posts = [Post(**post) for post in posts]
    return posts


