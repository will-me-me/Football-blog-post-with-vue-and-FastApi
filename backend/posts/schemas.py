from pydantic import BaseModel

class Post(BaseModel):
    post_id: int
    user_id: int
    title: str
    content: str
    image_url: str
    created_at: str

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

    