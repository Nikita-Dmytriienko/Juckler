import uuid
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


# CATEGORY TYPE
class CategoryType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


# CREATE
class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=256)
    type: CategoryType
    color: str = Field(pattern=r"^#[0-9A-Fa-f]{6}$", default="#808080")
    icon: str | None = Field(default=None, max_length=50)


# READ
class CategoryRead(BaseModel):
    id: uuid.UUID
    name: str
    type: CategoryType
    color: str
    icon: str | None
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# UPDATE
class CategoryUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=256)
    type: CategoryType | None = None
    color: str | None = Field(default=None, pattern=r"^#[0-9A-Fa-f]{6}$")
    icon: str | None = Field(default=None, max_length=50)
