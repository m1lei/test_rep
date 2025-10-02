import os

import jwt
from passlib.context import CryptContext
SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"

psw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_token(data):
    payload = data.copy()
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token
def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def has_password(password):
    hash_pass = psw_context.hash(password)
    return hash_pass

def verify_password(password:str, hashed:hash):
    return psw_context.verify(password, hashed)
print(verify_password(has_password('1233'),has_password('1233')))