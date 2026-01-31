from enum import Enum

from pydantic import BaseModel, EmailStr, Field


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
    pass


# READ
class UserRead(BaseModel):
    pass


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
