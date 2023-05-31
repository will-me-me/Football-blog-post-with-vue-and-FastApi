import shutil
from bson import ObjectId
from fastapi import HTTPException, status, UploadFile
from db import db
from datetime import datetime
import bcrypt
from pydantic import EmailStr
import uuid

from posts.schemas import Post

def save_post_images(post_images: list):
    image_urls = []
    for image in post_images:
        image_url = f"static/post_images/{image.filename}"
        with open(image_url, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_urls.append(image_url)
    return image_urls

def create_post(new_post: Post, post_images: list):
    image_urls = save_post_images(post_images)
    new_post.image_url = image_urls
    new_post.created_at = str(datetime.now())
    new_post.post_id = uuid.uuid4().hex
    db.posts.insert_one(new_post.dict())
    return new_post
     

    
   

def get_all_posts():
    posts = list(db.posts.find({}))
    for post in posts:
        post["_id"] = str(post["_id"])
    return posts
