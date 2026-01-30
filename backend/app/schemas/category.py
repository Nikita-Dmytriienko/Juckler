from enum import Enum

from pydantic import BaseModel, Field


class CategoryType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=256)
    type: CategoryType
    color: str = Field(pattern=r"^#[0-9A-Fa-f]{6}$")
    icon: str | None = None


class CategoryRead(BaseModel):
    id: int
    name: str
    type: CategoryType
    color: str | None
    icon: str | None
    user_id: int

    class Config:
        from_attributes = True
