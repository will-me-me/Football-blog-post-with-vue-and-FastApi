# import datetime
from datetime import datetime
from typing import List, Optional
from bson import ObjectId
import bson
from fastapi import HTTPException, UploadFile, status
from pydantic import BaseModel, Field, validator
import uuid
from uuid import uuid4
# from pydantic.schema import Schema

# from users.models import encrypt_password


class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    email: str
    password: str
    confirm_password: str
    bio: Optional[str]
    # profile_pic_url: Optional[UploadFile] = Field(None)
    created: Optional[datetime] = None
    # user_id = ObjectId()

    @validator("created", pre=True, always=True)
    def set_created(cls, value):
        return str(datetime.now())
    
    @validator("id", pre=True, always=True)
    def convert_object_id_to_str(cls, value):
        if value is not None:  # Check if value is not None before type-checking
            if isinstance(value, ObjectId()):
                return str(value)
            else:
                raise ValueError("Invalid id format")  # Raise an exception if it's not an ObjectId
        return value  # Return value as-is if it's None


    # @validator("profile_pic_url", pre=True, always=True)
    # def set_profile_pic_url(cls, value):
    #     if value == []:
    #         return [
    #             "https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png"
    #         ]
    #     return value

    def confirm_passwords_match(self):
        print("password: ", self.password)
        print("confirm_password: ", self.confirm_password)
        if self.password == self.confirm_password:
            return True
        raise ValueError("Passwords do not match")

    def user_dict(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)
        # print(data)
        data["id"] = self.__class__.convert_object_id_to_str(data["id"])
        """pop the confirm passwor"""
        data.pop("confirm_password")
        data["created"] = str(datetime.now())
        return data
    


class UserLogin(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    bio: Optional[str]
    # updated_at : Optional[datetime] = None


class UserOut(BaseModel):
    id: str 
    username: str
    email: str
    # profile_pic_url: Optional[List[str]]
    posts: list = []
    created: Optional[datetime] = None
    # user_id = bool = True
