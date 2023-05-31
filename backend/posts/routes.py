from datetime import datetime
from typing import List
from bson import ObjectId
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi import FastAPI
from auth.jwt_handler import jwt_dependecy, jwt_required, get_current_user
import posts.models as post_models
from db import db

from posts.schemas import Post

router = APIRouter()

@router.get('/get_current' ,dependencies=[Depends(jwt_dependecy)])
def get_current_user(user: dict = Depends(get_current_user)):
    return user

@router.get('/get_curent_user_id' ,dependencies=[Depends(jwt_dependecy)])
def get_current_user_id(user: dict = Depends(get_current_user)):
    return user['_id']


@router.post('/create_post', response_model=Post, dependencies=[Depends(jwt_dependecy)])
def create_post_handler(post: Post, images: List[UploadFile] = File(...)):
    images_urls = post_models.save_post_images(images)
    saved_post = post_models.create_post(post, images_urls)
    return saved_post



    



