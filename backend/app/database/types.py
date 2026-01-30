import datetime
import uuid
from typing import Annotated

from sqlalchemy import String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column

# Base types for all models <3
uuid_pk = Annotated[
    uuid.UUID, mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
]

created_at = Annotated[
    datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))
]

updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.now(datetime.UTC),
    ),
]


str_100 = Annotated[str, mapped_column(String(100))]
str_256 = Annotated[str, mapped_column(String(256))]
str_512 = Annotated[str, mapped_column(String(512))]
email_type = Annotated[str, mapped_column(String(255), unique=True, index=True)]
