# Framework convention override - FastAPI requires this pattern
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.app.api.v1.auth import router as auth_router
from backend.app.api.v1.common import router as common_router
from backend.app.core.config import settings
from backend.app.exceptions import BaseAppError

app = FastAPI(
    title=f"{settings.PROJECT_NAME} — Personal Finance Tracker",
    debug=settings.DEBUG,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.DEBUG else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception handlers
@app.exception_handler(BaseAppError)
async def app_error_handler(_request: Request, exc: BaseAppError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


# Routers
app.include_router(common_router, prefix="/health", tags=["health"])
app.include_router(auth_router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
