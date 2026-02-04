import uuid
from datetime import datetime

from fastapi_users import schemas as fus
from pydantic import BaseModel, ConfigDict, Field

from backend.app.models.user import UserRole


# CREATE — extends fastapi-users BaseUserCreate so registration saves custom fields
class UserCreate(fus.BaseUserCreate):
    username: str = Field(
        min_length=4,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$",
        description="Unique username (letters, numbers, underscore)",
    )
    first_name: str | None = Field(
        default=None, min_length=3, max_length=32, description="First name"
    )
    last_name: str | None = Field(
        default=None, min_length=3, max_length=32, description="Last name"
    )
    phone: str | None = Field(
        default=None,
        pattern=r"^\+?[1-9]\d{1,14}$",
        description="Phone number in E.164 format",
    )
    currency: str = Field(
        default="USD", max_length=3, description="Default currency (USD, EUR, etc)"
    )
    timezone: str = Field(default="UTC", description="User timezone")


# READ — extends fastapi-users BaseUser for API responses
class UserRead(fus.BaseUser[uuid.UUID]):
    username: str
    first_name: str | None
    last_name: str | None
    phone: str | None
    role: UserRole
    currency: str
    timezone: str
    email_verified: bool
    phone_verified: bool
    created_at: datetime
    updated_at: datetime
    last_login_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


# UPDATE — extends fastapi-users BaseUserUpdate for profile updates
class UserUpdate(fus.BaseUserUpdate):
    username: str | None = Field(
        default=None, min_length=3, max_length=32, pattern=r"^[a-zA-Z0-9_]+$"
    )
    first_name: str | None = Field(default=None, max_length=32)
    last_name: str | None = Field(default=None, max_length=32)
    phone: str | None = Field(default=None, pattern=r"^\+?[1-9]\d{1,14}$")
    currency: str | None = Field(default=None, max_length=3)
    timezone: str | None = None
    avatar_url: str | None = Field(default=None, description="URL to user avatar")


# ADMIN USER MANAGEMENT
class UserAdminUpdate(BaseModel):
    role: UserRole | None = None
    is_active: bool | None = None
    is_verified: bool | None = None
    email_verified: bool | None = None
    phone_verified: bool | None = None


# LIST WITH PAGINATION
class UserList(BaseModel):
    items: list[UserRead]
    total: int
    page: int
    page_size: int
    pages: int

    model_config = ConfigDict(from_attributes=True)


# USER PUBLIC PROFILE
class UserPublic(BaseModel):
    id: uuid.UUID
    username: str
    first_name: str | None
    last_name: str | None
    avatar_url: str | None


# DASHBOARD STATISTICS
class UserWithStats(UserRead):
    total_categories: int = 0
    total_transactions: int = 0
    total_balance: float = 0.0
