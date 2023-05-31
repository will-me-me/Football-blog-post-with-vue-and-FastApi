from fastapi import APIRouter
from fastapi import FastAPI
import posts.models as post_models

from posts.schemas import Post

router = APIRouter()

@router.post('/create_post', response_model=Post)
def create_post(new_post: Post, post_images: list = None):
    return post_models.create_post(new_post, post_images)




