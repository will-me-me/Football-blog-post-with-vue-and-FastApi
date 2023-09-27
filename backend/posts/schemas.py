# from ast import List
from typing import Optional, List
from bson import ObjectId
from fastapi import Depends, UploadFile
from pydantic import BaseModel, validator, Field
from datetime import datetime
from auth.jwt_handler import get_current_user

# from posts.models import get_current_user_id
import posts.models as post_models

# from users.schemas import User


class Post(BaseModel):
    # id: Optional[str]
    title: str
    content: str
    images: List[str]
    created_at: Optional[str] 
    owner: Optional[str] 
    post_id: Optional[str] 

    @validator("created_at", pre=True, always=True)
    def set_created_at(cls, value):
        return str(datetime.now())

    # @validator('owner', pre=True, always=True)
    # def set_owner(cls,  user: dict = Depends(get_current_user)):
    #     user = post_models.get_current_user_id(user)
    #     print('user', user)
    #     return user


class PostOut(BaseModel):
    title: str
    content: str
    images: List[str]
    created_at: str
    owner: str


class PostUpdate(BaseModel):
    title: str
    content: str
    image_url: str


class PostDelete(BaseModel):
    post_id: int
    user_id: int


class PostLike(BaseModel):
    post_id: int
    user_id: int
