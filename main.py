from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from DbManager import DbManager
import auth
app = FastAPI()
db = DbManager()

class Register(BaseModel):
    name: str
    email: EmailStr
    password: str

class Login(BaseModel):
    email: EmailStr
    password: str


@app.get("/")
def root():
    return {"Hello": "World"}

@app.post('/register')
def register(user: Register):
    new = db.add(name=user.name, email=user.email, password=user.password)
    if not new:
        raise HTTPException(status_code=400, detail="Email alredy registration")
    payload = {'id':new.id,'email':new.email}
    token = auth.create_token(payload)
    return {"access_token": token, "token_type": "bearer"}

@app.post('/login')
def login(user: Login):
    if not db.logout(user.email, user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    payload = {'email': user.email}
    token = auth.create_token(payload)
    return {"access_token": token, "token_type": "bearer"}

