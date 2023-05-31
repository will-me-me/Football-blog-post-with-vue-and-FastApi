import shutil
from typing import List
from bson import ObjectId
from fastapi import Depends, HTTPException, status, UploadFile, File
from auth.jwt_handler import get_current_user, jwt_dependecy
from db import db
from datetime import datetime
import bcrypt
from pydantic import EmailStr
import uuid

from posts.schemas import Post

def save_post_images(images: List[UploadFile])-> List[str]:
    images_urls = []
    for image in images:
        image_url = f"static/post_images/{image.filename}"
        print(image_url)
        with open(image_url, "wb") as f:
            f.write(image.file.read())
        images_urls.append(image_url)
    return images_urls

def create_post(post: Post, image_urls: List[str]):
    created_at = str(datetime.now())
    owner = get_current_user()
    print('owner')
    print(owner)
    post_data = post.dict()
    post_data["image_url"] = image_urls
    post_data["created_at"] = created_at
    post_data["owner"] = owner
    
    # Save the post to the database using your preferred method
    saved_post = db.posts.insert_one(post_data)
    
    return Post(**saved_post)

   
   
def get_all_posts():
    posts = list(db.posts.find({}))
    for post in posts:
        post["_id"] = str(post["_id"])
    return posts
