# import datetime
from datetime import datetime
from typing import Optional
from bson import ObjectId
from fastapi import HTTPException, status
from pydantic import BaseModel,Field
import uuid
from uuid import uuid4


class User(BaseModel):
    _id : str = Field(..., alias="_id")
    username : str
    email : str
    password : str
    confirm_password: str
    profile_pic_url : str
    created : Optional[str]

    def confirm_passwords_match(self):
        if self.password != self.confirm_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Passwords do not match"
            )
        return True
    
    def user_dict(self, *args, **kwargs):
        data = super().dict(*args, **kwargs)
        # self.user_id = self.user_id or uuid4().hex
        data.pop("confirm_password", None)
        # data['_id'] = ObjectId()
        data['created'] = str(datetime.now())
        return data

class UserLogin(BaseModel):
    email : str
    password : str

class UserUpdate(BaseModel):
    username : str
    email : str
    password : str
    profile_pic_url : str

class UserOut(BaseModel):
    _id :  str = Field(..., alias="_id")
    username : str
    email : str
    profile_pic_url : str
    posts: list = []
    created : Optional[str]


