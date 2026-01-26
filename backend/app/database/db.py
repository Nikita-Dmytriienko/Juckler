from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

async_engine = create_async_engine(
    url="postgresql+asyncpg://postgres:root@localhost:5432/juckler",
    pool_size=20,
    max_overflow=30,
)

new_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)
