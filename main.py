
from fastapi import FastAPI
from pydantic import BaseModel

from enum import Enum
from datetime import datetime

from uuid import UUID
import uuid


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


class ProgressStatus(Enum):
    PROGRESS_STATUS_CANCELED = 0
    PROGRESS_STATUS_IN_PROGRESS = 1
    PROGRESS_STATUS_DONE = 2


class Task(BaseModel):
    id: UUID
    header: str
    text: str
    external_images: list[str]
    deadline: int
    progress_status: ProgressStatus
    is_urgent: bool
    is_important: bool
    owner_id: int
    parent_id: UUID | None = None
    possible_deadline: int
    weight: int


class CreateTaskRequest(BaseModel):
    header: str
    text: str
    external_images: list[str]
    deadline: int
    progress_status: ProgressStatus
    is_urgent: bool
    is_important: bool
    owner_id: int
    parent_id: UUID | None = None
    possible_deadline: int
    weight: int


class CreateTaskResponse(BaseModel):
    task_id: UUID


class UpdateTaskRequest(BaseModel):
    task: Task


class UpdateTaskResponse(BaseModel):
    task_id: UUID


class GetTaskRequest(BaseModel):
    task_id: UUID


class GetTaskResponse(BaseModel):
    task: Task


class GetTaskByUserIDRequest(BaseModel):
    user_id: int


class GetTaskByUserIDResponse(BaseModel):
    tasks: list[Task]


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


@app.post('/api/tasks', response_model=CreateTaskResponse)
def api_tasks_create(request: CreateTaskRequest):
    return {'id': uuid.uuid5()}


@app.put('/api/tasks', response_model=UpdateTaskResponse)
def api_tasks_update(request: UpdateTaskRequest):
    return {'id': uuid.uuid5()}


@app.get('/api/tasks/{task_id}', response_model=GetTaskResponse)
def api_tasks_get(task_id: UUID):
    return {
        'id': uuid.uuid5(),
        'header': 'Header',
        'text': 'Text',
        'external_images': [],
        'deadline': datetime.utcnow().timestamp(),
        'progress_status': ProgressStatus.PROGRESS_STATUS_IN_PROGRESS,
        'is_urgen': True,
        'is_important': False,
        'owner_id': 0,
        'parent_id': uuid.uuid5(),
        'possible_deadline': datetime.utcnow().timestamp(),
        'weight': 0
    }


@app.get('/api/tasks', response_model=GetTaskByUserIDResponse)
def api_tasks_get_by_user_id(user_id: int):
    return [
        {
            'id': uuid.uuid5(),
            'header': 'Header',
            'text': 'Text',
            'external_images': [],
            'deadline': datetime.utcnow().timestamp(),
            'progress_status': ProgressStatus.PROGRESS_STATUS_IN_PROGRESS,
            'is_urgen': True,
            'is_important': False,
            'owner_id': 0,
            'parent_id': uuid.uuid5(),
            'possible_deadline': datetime.utcnow().timestamp(),
            'weight': 0
        },
    ]
