import enum
from datetime import datetime
from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Boolean, Enum, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database.base import Base
from backend.app.database.types import created_at, updated_at

if TYPE_CHECKING:
    from .category import Category
    from .transaction import Transaction


class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"
    MANAGER = "manager"


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    # Inherit from SQLAlchemyBaseUserTableUUID + Base
    # - id: UUID (primary_key=True)
    # - email: str (unique, indexed, required)
    # - hashed_password: str (required)
    # - is_active: bool = True
    # - is_superuser: bool = False
    # - is_verified: bool = False

    username: Mapped[str] = mapped_column(
        String(20), unique=True, index=True, nullable=False
    )

    # Personal info
    first_name: Mapped[str | None] = mapped_column(String(32), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(32), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True, index=True)
    avatar_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    # Settings
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole), default=UserRole.USER, index=True
    )
    currency: Mapped[str] = mapped_column(String(3), default="USD")
    timezone: Mapped[str] = mapped_column(String(50), default="UTC")

    # Status flags
    email_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    phone_verified: Mapped[bool] = mapped_column(Boolean, default=False)

    # Timestamps
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    last_login_at: Mapped[datetime | None] = mapped_column(nullable=True)

    # Relationships
    categories: Mapped[list["Category"]] = relationship(
        back_populates="user", cascade="all, delete-orphan", lazy="selectin"
    )

    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="user", cascade="all, delete-orphan", lazy="selectin"
    )

    __table_args__ = (
        Index("idx_user_username", "username"),
        Index("idx_user_phone", "phone"),
        Index("idx_user_role", "role"),
        Index("idx_user_status", "is_active", "is_verified"),
    )
