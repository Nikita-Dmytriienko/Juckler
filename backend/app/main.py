# ruff: noqa: B008  # Framework convention override - FastAPI requires this pattern
from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core.security import auth_backend, fastapi_users
from backend.app.database.database import get_db
from backend.app.schemas.user import UserCreate, UserRead, UserUpdate

app = FastAPI(title="Juckler - Personal Finance Tracker")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


# GET
@app.get("/")
def root():
    return {"message": "First start"}


@app.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "ok", "detail": "Service is healthy"}
    except Exception as e:
        return {"status": "error", "database": "disconnected", "detail": str(e)}


# POST
# @app.post()


# PUT
# @app.put()


# DELETE
# @app.delete()
