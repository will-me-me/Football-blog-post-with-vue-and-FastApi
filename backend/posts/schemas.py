# from ast import List
from typing import Optional, List
from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime

from users.schemas import User

class Post(BaseModel):
    _id: str
    title: str
    content: str
    image_urls: List[str]
    created_at: str
    owner: str 


    def post_dict(self, *args, **kwargs):
        data = super().dict(*args, **kwargs)
        data['_id'] = ObjectId()
        data['created_at'] = str(datetime.now())
        return data


class PostCreate(BaseModel):
    user_id: int
    title: str
    content: str
    image_url: str 

    # def post_dict(self, *args, **kwargs):
        # data = super().dict(*args, **kwargs)
        # data['_id'] = ObjectId()
        # data['created_at'] = str(datetime.now())
        # return data


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

    