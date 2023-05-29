from pydantic import BaseModel

class User(BaseModel):
    user_id : int
    username : str
    email : str
    password : str
    confirm_password: str
    profile_pic_url : str

class UserLogin(BaseModel):
    username : str
    password : str

class UserUpdate(BaseModel):
    username : str
    email : str
    password : str
    profile_pic_url : str

class UserDelete(BaseModel):
    user_id : int
    username : str
    email : str
    password : str
    profile_pic_url : str

class UserOut(BaseModel):
    user_id : int
    username : str
    email : str
    profile_pic_url : str
    posts: list = []
    