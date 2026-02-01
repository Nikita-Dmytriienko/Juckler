import uuid
from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"


class TransactionStatus(str, Enum):
    COMPLETED = "completed"
    PENDING = "pending"
    CANCELLED = "cancelled"
    FAILED = "failed"


class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    UAH = "UAH"


# CREATE
class TransactionCreate(BaseModel):
    amount: Decimal = Field(gt=0)
    type: TransactionType
    description: str | None = None
    date: datetime = Field(default_factory=datetime.now)
    category_id: uuid.UUID | None = None
    currency: str = "USD"


# UPDATE
class TransactionUpdate(BaseModel):
    amount: Decimal | None = Field(default=None, gt=0)
    type: TransactionType | None = None
    description: str | None = None
    date: datetime | None = None
    category_id: uuid.UUID | None = None


# READ
class TransactionRead(BaseModel):
    id: uuid.UUID
    amount: Decimal
    type: TransactionType
    description: str | None
    date: datetime
    status: TransactionStatus
    currency: str
    category_id: uuid.UUID | None
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# LIST
class TransactionList(BaseModel):
    items: list[TransactionRead]


# LIST WITH FILTERS
class TransactionFilters(BaseModel):
    pass


# STATISTICS
class TransactionSummary(BaseModel):
    pass


# CATEGORY SUMMARY
class CategorySummary(BaseModel):
    pass


# TRANSACTION STATS
class TransactionStats(BaseModel):
    pass
