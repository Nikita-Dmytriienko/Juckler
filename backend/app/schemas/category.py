import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from backend.app.models.category import CategoryType


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
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# UPDATE
class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=256)
    type: CategoryType | None = None
    color: str | None = Field(default=None, pattern=r"^#[0-9A-Fa-f]{6}$")
    icon: str | None = Field(default=None, max_length=50)


# LIST
class CategoryList(BaseModel):
    items: list[CategoryRead]
    total: int
    page: int
    page_size: int
    pages: int

    model_config = ConfigDict(from_attributes=True)
