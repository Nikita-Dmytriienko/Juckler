from enum import Enum

from pydantic import BaseModel


# USER TYPE
class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"
    MANAGER = "manager"


# CREATE
class UserCreate(BaseModel):
    pass


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
