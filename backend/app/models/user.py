import enum
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Enum, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database.base import Base
from backend.app.database.types import created_at, updated_at, uuid_pk

if TYPE_CHECKING:
    from .category import Category
    from .transaction import Transaction


class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"
    MANAGER = "manager"


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid_pk]
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    username: Mapped[str] = mapped_column(
        String(20), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    # Personal info
    first_name: Mapped[str | None] = mapped_column(String(32), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(32), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True, index=True)
    avatar_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    # Settings
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.USER)
    currency: Mapped[str] = mapped_column(String(3), default="USD")
    timezone: Mapped[str] = mapped_column(String(50), default="UTC")

    # Status flags
    is_active: Mapped[bool] = mapped_column(default=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    email_verified: Mapped[bool] = mapped_column(default=False)
    phone_verified: Mapped[bool] = mapped_column(default=False)

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
        Index("idx_user_email", "email"),
        Index("idx_user_username", "username"),
        Index("idx_user_phone", "phone"),
        Index("idx_user_role", "role"),
        Index("idx_user_status", "is_active", "is_verified"),
    )
