from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime

from users.schemas import User

class Post(BaseModel):
    # user_id: 
    title: str
    content: str
    image_url: str
    created_at: str
    owner : User


class PostCreate(BaseModel):
    user_id: int
    title: str
    content: str
    image_url: str 


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

    