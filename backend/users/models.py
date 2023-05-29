from db import db
from datetime import datetime
import bcrypt 
from users.models import User 

def encrypt_password(password: str):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

def compare_passwords(pass_1:str, pass_2:str):
    return bcrypt.checkpw(pass_1.encode(), pass_2.encode())

def create_user(new_user: User):
    pass

