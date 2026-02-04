import enum
from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database.base import Base

from ..database.types import created_at, str_256, updated_at, uuid_fk, uuid_pk

if TYPE_CHECKING:
    from .transaction import Transaction
    from .user import User


class CategoryType(str, enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[uuid_pk]
    name: Mapped[str_256]
    type: Mapped[CategoryType] = mapped_column(
        Enum(CategoryType), nullable=False, index=True
    )
    color: Mapped[str] = mapped_column(String(7), default="#808080")
    icon: Mapped[str] = mapped_column(String(50), nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    # Foreign key
    user_id: Mapped[uuid_fk] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    # Relationships
    user: Mapped["User"] = relationship(back_populates="categories")
    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("idx_category_user_name", "user_id", "name"),
        Index("idx_category_user_type", "user_id", "type"),
    )
