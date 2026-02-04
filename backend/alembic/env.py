import asyncio
import sys
from logging.config import fileConfig
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))

import sqlalchemy as sa  # noqa: F401 — used in render_item for migrations
from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from backend.app.core.config import settings
from backend.app.database.base import Base
from backend.app.models.category import Category  # noqa: F401
from backend.app.models.transaction import Transaction  # noqa: F401
from backend.app.models.user import User  # noqa: F401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def render_item(type_, obj, autogen_context):
    """Render fastapi-users GUID type as sa.UUID()."""
    if type_ == "type" and hasattr(obj, "__class__"):
        class_name = obj.__class__.__name__
        if class_name == "GUID":
            autogen_context.imports.add("import sqlalchemy as sa")
            return "sa.UUID()"
    return False


def run_migrations_offline() -> None:
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        render_as_batch=True,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_item=render_item,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        render_item=render_item,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    connectable = create_async_engine(settings.DATABASE_URL)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
