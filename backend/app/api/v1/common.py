from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.database import get_db

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Juckler API is running"}


@router.get("/health")
async def health(db: AsyncSession = Depends(get_db)):  # noqa: B008
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "ok", "detail": "Service is healthy"}
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={"status": "error", "database": "disconnected", "detail": str(e)},
        )
