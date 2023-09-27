from pydantic import BaseModel


class Comment(BaseModel):
    comment_id: int
    user_id: int
    post_id: int
    content: str
    created_at: str
