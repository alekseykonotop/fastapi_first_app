from pydantic import BaseModel, ConfigDict
from typing import Optional


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int
    name: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class STaskId(BaseModel):
    ok: bool = True
    task_id: int


# Users
class SUserAdd(BaseModel):
    name: str
    login: str
    age: int
    phone: Optional[str] = None

class SUser(SUserAdd):
    id: int
    name: str
    login: str
    age: int
    phone: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class SUserId(BaseModel):
    ok: bool = True
    user_id: int