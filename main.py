from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RegisterRequest(BaseModel):
    email: str
    password: str


class RegisterResponse(BaseModel):
    user_id: int


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    user_id: int


@app.post('/api/auth/register', response_model=RegisterResponse)
def api_auth_register(request: RegisterRequest):
    return {'user_id': 0}


@app.post('/api/auth/login', response_model=LoginResponse)
def api_auth_login(request: LoginRequest):
    return {'user_id': 0}
