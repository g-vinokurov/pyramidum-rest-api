
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from pydantic import BaseModel

from enum import Enum
from datetime import date
from datetime import datetime

from uuid import UUID
import uuid


app = FastAPI()

# Unsafety setting!!!
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)


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


class ProgressStatus(Enum):
    PROGRESS_STATUS_CANCELED = 0
    PROGRESS_STATUS_IN_PROGRESS = 1
    PROGRESS_STATUS_DONE = 2


class Task(BaseModel):
    id: UUID
    header: str
    text: str
    external_images: list[str]
    deadline: date
    progress_status: ProgressStatus
    is_urgent: bool
    is_important: bool
    owner_id: int
    parent_id: UUID | None = None
    possible_deadline: date
    weight: int


class CreateTaskRequest(BaseModel):
    header: str
    text: str
    external_images: list[str]
    deadline: date
    progress_status: ProgressStatus
    is_urgent: bool
    is_important: bool
    owner_id: int
    parent_id: UUID | None = None
    possible_deadline: date
    weight: int


class CreateTaskResponse(BaseModel):
    task_id: UUID


class UpdateTaskRequest(BaseModel):
    task_id: UUID


class UpdateTaskRequestBody(BaseModel):
    header: str
    text: str
    external_images: list[str]
    deadline: date
    progress_status: ProgressStatus
    is_urgent: bool
    is_important: bool
    owner_id: int
    parent_id: UUID | None = None
    possible_deadline: date
    weight: int


class UpdateTaskResponse(BaseModel):
    task_id: UUID


class TaskRequest(BaseModel):
    task_id: UUID


class TaskResponse(Task):
    pass


class TasksResponse(BaseModel):
    tasks: list[Task]


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


@app.get('/api/tasks', response_model=TasksResponse)
def api_tasks_get_all(
    user_id: int,
    search: str | None = None,
    deadline_from: date | None = None,
    deadline_to: date | None = None,
    possible_deadline_from: date | None = None,
    possible_deadline_to: date | None = None,
    progress_status: ProgressStatus | None = None,
    is_urgent: bool | None = None,
    is_important: bool | None = None,
    weight_from: int | None = None,
    weight_to: int | None = None,
):
    return [
        {
            'id': uuid.uuid5(uuid.NAMESPACE_DNS, 'api-tasks-get-by-user-id'),
            'header': 'Header',
            'text': 'Text',
            'external_images': [],
            'deadline': datetime.utcnow().date(),
            'progress_status': ProgressStatus.PROGRESS_STATUS_IN_PROGRESS,
            'is_urgen': True,
            'is_important': False,
            'owner_id': 0,
            'parent_id': uuid.uuid5(uuid.NAMESPACE_DNS, 'api-tasks-get-by-user-id-parent'),
            'possible_deadline': datetime.utcnow().date(),
            'weight': 0
        },
    ]


@app.post('/api/tasks', response_model=CreateTaskResponse)
def api_tasks_create(request: CreateTaskRequest):
    return {'task_id': uuid.uuid5(uuid.NAMESPACE_DNS, 'api-tasks-create')}


@app.put('/api/tasks/{task_id}', response_model=UpdateTaskResponse)
def api_tasks_update(task_id: UUID, request: UpdateTaskRequestBody):
    return {'task_id': uuid.uuid5(uuid.NAMESPACE_DNS, 'api-tasks-update')}


@app.get('/api/tasks/{task_id}', response_model=TaskResponse)
def api_tasks_get_one(task_id: UUID):
    return {
        'id': uuid.uuid5(uuid.NAMESPACE_DNS, 'api-tasks-get-one'),
        'header': 'Header',
        'text': 'Text',
        'external_images': [],
        'deadline': datetime.utcnow().date(),
        'progress_status': ProgressStatus.PROGRESS_STATUS_IN_PROGRESS,
        'is_urgen': True,
        'is_important': False,
        'owner_id': 0,
        'parent_id': uuid.uuid5(uuid.NAMESPACE_DNS, 'api-tasks-get-one-parent'),
        'possible_deadline': datetime.utcnow().date(),
        'weight': 0
    }
