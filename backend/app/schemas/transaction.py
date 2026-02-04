import uuid
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from backend.app.models.transaction import TransactionStatus, TransactionType


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
    total: int
    page: int
    page_size: int
    pages: int

    model_config = ConfigDict(from_attributes=True)
