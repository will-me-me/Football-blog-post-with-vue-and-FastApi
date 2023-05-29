from fastapi import HTTPException, status
from db import db
from datetime import datetime
import bcrypt

from users.schemas import User 


def encrypt_password(password: str):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

def compare_passwords(pass_1:str, pass_2:str):
    return bcrypt.checkpw(pass_1.encode(), pass_2.encode())


def create_user(new_user: User):
    email = new_user.email
    user = db.users.find_one({"email": email})
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )
    new_user.id = db.users.count_documents({}) + 1
    new_user.confirm_passwords_match()
    new_user.password = encrypt_password(new_user.password)
    new_user.created_at = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    new_user.profile_pic_url = "https://i.imgur.com/2xW3Yzg.png"
    db.users.insert_one(new_user.dict())
    return new_user




    

