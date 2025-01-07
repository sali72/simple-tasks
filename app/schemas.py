from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field


class BaseModelConfigured(BaseModel):
    """
    Adds configuration to base model to use for all schemas.

    Configurations:
    forbid extra fields
    """

    class Config:
        extra = Extra.forbid


class TaskCreationSchema(BaseModelConfigured):
    title: str = Field(..., title="The task title")
    is_completed: bool = Field(False, title="The task completion status")
    description: str = Field(None, title="The task description")


class TaskUpdateSchema(BaseModelConfigured):
    title: Optional[str] = Field(None, title="The task title")
    is_completed: Optional[bool] = Field(None, title="The task completion status")
    description: Optional[str] = Field(None, title="The task description")


class ResponseSchema(BaseModelConfigured):
    message: str = Field(None, example="success")
    data: dict = Field(None, example={"data": "Your requested data"})
    timestamp: datetime = Field(datetime.now(), example="2024-02-16T14:05:09.252968")
