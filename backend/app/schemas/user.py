import uuid
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# USER TYPE
class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"
    MANAGER = "manager"


# CREATE
class UserCreate(BaseModel):
    email: EmailStr = Field(description="User email address")
    username: str = Field(
        min_length=4,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$",
        description="Unique username (letters, numbers, underscore)",
    )
    password: str = Field(min_length=8, max_length=32, description="Strong password")

    # Optional fields
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
    currency: str | None = Field(
        default="USD", max_length=3, description="Default currency (USD, EUR, etc)"
    )
    timezone: str | None = Field(default="UTC", description="User timezone")


# LOGIN
class UserLogin(BaseModel):
    email_or_username: str = Field(description="Email or username")
    password: str


# READ
class UserRead(BaseModel):
    id: uuid.UUID
    email: EmailStr
    username: str
    first_name: str | None
    last_name: str | None
    phone: str | None
    role: UserRole
    currency: str
    timezone: str
    is_active: bool
    is_verified: bool
    email_verified: bool
    phone_verified: bool
    created_at: datetime
    updated_at: datetime
    last_login_at: datetime | None

    # Statistics (for dashboard)
    total_categories: int | None = 0
    total_transactions: int | None = 0
    total_balance: float | None = 0.0

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "email": "user@example.com",
                "username": "john_doe",
                "first_name": "John",
                "last_name": "Doe",
                "role": "user",
                "is_active": True,
                "is_verified": True,
                "created_at": "2024-01-30T10:30:00Z",
            }
        },
    )


# UPDATE
class UserUpdate(BaseModel):
    email: EmailStr | None = None
    username: str | None = Field(
        default=None, min_length=3, max_length=32, pattern=r"^[a-zA-Z0-9_]+$"
    )
    first_name: str | None = Field(default=None, max_length=32)
    last_name: str | None = Field(default=None, max_length=32)
    phone: str | None = Field(default=None, pattern=r"^\+?[1-9]\d{1,14}$")
    currency: str | None = Field(default=None, max_length=3)
    timezone: str | None = None
    avatar_url: str | None = Field(default=None, description="URL to user avatar")


# USER PASSWORD CHANGE
class UserPasswordChange(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8)


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


# USER TOKEN
class UserToken(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


# USER PUBLIC
class UserPublic(BaseModel):
    id: uuid.UUID
    username: str
    first_name: str | None
    last_name: str | None
    avatar_url: str | None
