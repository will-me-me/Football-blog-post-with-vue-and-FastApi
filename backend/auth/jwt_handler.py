# this file is responsible for singing, enconding , decoding, and returning JWTS

from typing import Optional
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, Header, Request, Security

from base64 import decode
import time
import jwt
from decouple import config
from db import db

JWT_SECRET= '88768c3cecc095dba0feee71c0e3fd89186f15a2043d881b26bc899b7ed2a270'
JWT_ALGORITHM= 'HS256'


# If the request has an Authorization header, try to parse it as a Bearer token, and if that fails,
# return None.
class OptionalBearer():
    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        authorization: str = request.headers.get("Authorization")
        if authorization:
            try:
                return await HTTPBearer()(request)
            except:
                return 


security = HTTPBearer()

optional = OptionalBearer()


def sign_jwt(user: dict, expires=None):
    """
    It takes a user object, adds an expiry time to it, and then signs it with a secret key
    
    :param user: The user object that we want to sign
    :type user: dict
    :return: A JWT token
    """
    # user.update({
    #     'expiry': time.time() + 86400
    # })
    user.update({"expiry": expires or time.time() + 100000})
    return jwt.encode(user, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decodeJWT(token: str):
    """
    It decodes the token, checks if it's expired, and returns the payload
    
    :param token: The token to decode
    :type token: str
    :return: The payload of the token.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except:
        raise ValueError("Invalid Token")
    if payload['expiry'] < time.time():
        raise ValueError("Token Expired")
    return payload


def jwt_dependecy(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    > If the user is authenticated, return the user object, otherwise raise an error
    
    :param credentials: HTTPAuthorizationCredentials = Security(security)
    :type credentials: HTTPAuthorizationCredentials
    :return: The user object
    """
    user = decodeJWT(credentials.credentials)
    if user:
        return user
    raise ValueError("Unauthorized: 401")


def jwt_optional(credentials: Optional[HTTPAuthorizationCredentials] = Security(optional)):
    """
    If the user is logged in, return the user object, otherwise return an empty object
    
    :param credentials: Optional[HTTPAuthorizationCredentials] = Security(optional)
    :type credentials: Optional[HTTPAuthorizationCredentials]
    :return: A dictionary with the user's information.
    """
    try:
        user = decodeJWT(credentials.credentials)
        return user or {}
    except:
        return {}
    
def get_current_user(jwt_dependecy: HTTPAuthorizationCredentials = Security(security)):
    """
    > If the user is authenticated, return the user object, otherwise raise an error
    
    :param credentials: HTTPAuthorizationCredentials = Security(security)
    :type credentials: HTTPAuthorizationCredentials
    :return: The user object
    """
    user = decodeJWT(jwt_dependecy.credentials)
    print('user')
    print(user)
    if user:
        email = user['email']
        new_user = db.users.find_one({"email": email})
        id = new_user['_id']
        id = user['_id'] = str(id)
        print(id)
        return id
    raise ValueError("Unauthorized: 401")




jwt_required = Depends(jwt_dependecy)