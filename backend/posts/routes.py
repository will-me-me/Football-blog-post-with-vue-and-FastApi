from datetime import datetime
import os
from typing import List
from bson import ObjectId
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi import FastAPI
from gridfs import GridFS
from requests import request
from auth.jwt_handler import jwt_dependecy, jwt_required, get_current_user
import posts.models as post_models
from db import db
fs = GridFS(db)



from posts.schemas import Post, PostOut
from users.schemas import User

router = APIRouter()

@router.get('/me_login' , dependencies=[Depends(jwt_dependecy)])
def me_login(user: dict = Depends(get_current_user)):
    return user

@router.get('/current_user_id', dependencies=[Depends(jwt_dependecy)])
def current_user_id(user: dict = Depends(get_current_user)):
    print('user', user)
    return post_models.get_current_user_id(user)
    

@router.post("/create_post/", dependencies=[Depends(jwt_dependecy)])
async def create_post(title: str, content: str,   images: List[UploadFile] = File(...), user: dict = Depends(get_current_user)):
    saved_images = await post_models.save_images(images)
    post=Post(title=title, content=content, images=saved_images)
    post_data = post.dict()
    '''add owner to post whose the current user'''
    user = post_models.get_current_user_id(user)
    print('user', user)
    post_data['owner'] = user
    '''add post_id '''
    post_data['post_id'] = str(ObjectId())
    print('post_data', post_data)
    
    result = db.posts.insert_one(post_data)
    post_data["_id"] = str(result.inserted_id)
    # post_data['post_id'] = post_data['_id']
    print('post_data', post_data)
    return post_data

@router.get("/get_all_posts/")
async def get_all_posts():
    posts = post_models.get_all_posts()
    return posts

@router.get("/get_post/{post_id}")
async def get_post(post_id: str):
    post = post_models.get_post_by_id(post_id)
    return post

@router.get("/get_user_posts/{user_id}")
async def get_user_posts(user_id: str):
    posts = post_models.get_post_by_user_id(user_id)
    return posts

@router.delete("/delete_post/{post_id}", dependencies=[Depends(jwt_dependecy)])
async def delete_post(post_id: str, user: dict = Depends(get_current_user)):
    post = post_models.get_post_by_id(post_id)
    owner = post_models.get_post_owner(post_id)
    print('owner', owner)
    print('user', user)
    if owner == user:
        post_models.delete_post_by_id(post_id)
        return {"message": "Post deleted successfully"}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
@router.put("/update_post/{post_id}", dependencies=[Depends(jwt_dependecy)])
async def update_post(post_id: str, title: str, content: str, images: List[UploadFile] = File(...), user: dict = Depends(get_current_user)):
    post = post_models.get_post_by_id(post_id)
    owner = post_models.get_post_owner(post_id)
    if owner == user:
        saved_images = await post_models.save_images(images)
        post = post_models.update_post_by_id(post_id, title, content, saved_images)
        return post
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
    

    

      
    
    