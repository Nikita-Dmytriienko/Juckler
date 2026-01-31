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

    # first_name:
    # last_name:
    # phone:
    # timezone:


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
    isactive: bool
    is_verified: bool
    email_verified: bool
    phone_verified: bool
    created_at: datetime
    updated_at: datetime
    last_login_at: datetime | None

    # STATISTICS (for dashboard)
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
                "created_at": "2026-01-30T10:30:00Z",
            }
        },
    )


# UPDATE
class UserUpdate(BaseModel):
    pass


# PASSWORD CHANGE
class UserPasswordChange(BaseModel):
    pass


# USER ADMIN UPDATE
class UserAdminUpdate(BaseModel):
    pass


# LIST
class UserList(BaseModel):
    pass


# USER TOKEN
class UserToken(BaseModel):
    pass


# USER PUBLIC
class UserPublic(BaseModel):
    pass
