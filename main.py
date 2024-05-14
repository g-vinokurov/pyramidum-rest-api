import uuid

from fastapi import FastAPI
from pydantic import BaseModel, field_validator

from datetime import datetime
from uuid import UUID

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


# 1715678526
# class Motivator(BaseModel):
#     id: UUID
#     user_id: int
#     start_time: datetime
#     end_time: datetime = None
#
#     @field_validator('start_time', 'end_time')
#     @classmethod
#     def dt_validate(cls, dt):
#         return datetime.fromtimestamp(dt) if dt is not None else None


class StartSessionRequest(BaseModel):
    user_id: int


class StartSessionResponse(BaseModel):
    id: UUID


class StopSessionRequest(BaseModel):
    id: UUID


class StopSessionResponse(BaseModel):
    id: UUID


@app.post('/api/auth/register', response_model=RegisterResponse)
def api_auth_register(request: RegisterRequest):
    return {'user_id': 0}


@app.post('/api/auth/login', response_model=LoginResponse)
def api_auth_login(request: LoginRequest):
    return {'user_id': 0}


@app.get('/api/motivator/start-session', response_model=StartSessionResponse)
def api_motivator_start_session(user_id: int):
    return {'id': uuid.uuid5()}


@app.get('/api/motivator/stop-session/{session_uuid}', response_model=StopSessionResponse)
def api_motivator_stop_session(session_uuid: UUID):
    return {'id': session_uuid}
