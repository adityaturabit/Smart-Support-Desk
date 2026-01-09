from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from database.db_config import engine,SessionLocal
import database.db_models as db_models

app = FastAPI()

app.add_middleware(CORSMiddleware,allow_origins = ["*"],allow_methods = ["*"],allow_headers = ["*"])

db_models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Message(BaseModel):
    text: str

# @app.get("/")
# def greet():
#     return "Fast is running in backend"

# @app.post("/send")
# def rec(data : Message):
#     res_text = f"Received Information is {data.text}"
#     return {"response": res_text}

# @app.get("/login")
# def login_page():
#     return "Login Page"

@app.get("/register")
def register_page():
    return "register Page"

user_db = {"username":"aditya123",}

class LoginData(BaseModel):
    username : str
    password : str


@app.post("/login")
def login_page(data : LoginData):
    username = data.username
    password = data.password
    if username in user_db and user_db["username"] == password:
        return "Successfully logged in"
    else:
        raise HTTPException(status_code=401,detail="Invalid Credentails")