from enum import Enum

from pydantic import BaseModel


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
    pass


# UPDATE
class TransactionUpdate(BaseModel):
    pass


# READ
class TransactionRead(BaseModel):
    pass


# LIST WITH FILTERS
class TransactionFilters(BaseModel):
    pass


# LIST
class TransactionList(BaseModel):
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
