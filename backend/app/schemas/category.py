import uuid

from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column


class CategoryCreate(BaseModel):
    id: uuid.UUID = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
