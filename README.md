# Juckler — Personal Finance Tracker
ОТ
A personal finance tracker built with FastAPI, SQLAlchemy, and PostgreSQL.

## Tech Stack

- **Python 3.13+** / **FastAPI** / **Uvicorn**
- **SQLAlchemy (async)** + **Asyncpg** — async ORM & PostgreSQL driver
- **fastapi-users** — authentication (JWT), registration, user management
- **Alembic** — database migrations
- **Pydantic v2** — data validation & settings
- **Docker & Docker Compose** — containerized deployment
- **Ruff** — linting & formatting
- **UV** — package manager

## Project Structure

```
Juckler/
├── backend/
│   ├── app/
│   │   ├── api/v1/          # Versioned API routes (auth, categories, transactions)
│   │   ├── core/            # Config (pydantic-settings) and security (JWT, fastapi-users)
│   │   ├── database/        # Async engine, session, base model, custom column types
│   │   ├── models/          # SQLAlchemy ORM models (User, Category, Transaction)
│   │   ├── schemas/         # Pydantic request/response schemas
│   │   ├── repositories/    # Data access layer
│   │   ├── services/        # Business logic
│   │   ├── utils/           # Helpers
│   │   ├── exceptions.py    # Custom exception hierarchy
│   │   └── main.py          # FastAPI app entry point
│   ├── alembic/             # Database migrations
│   └── tests/               # Test suite
├── frontend/                # Frontend (planned)
├── infra/nginx/             # Nginx config
├── docker-compose.yaml
├── Dockerfile
├── pyproject.toml
└── .env.example
```

## Quick Start

```bash
# 1. Clone and configure
cp .env.example .env
# Edit .env with your secrets

# 2. Run with Docker
docker compose up --build

# 3. API is available at
# http://localhost:8000/health/health — health check
# http://localhost:8000/api/v1/auth/  — authentication endpoints
# http://localhost:8000/docs          — Swagger UI
```

## Development

```bash
# Install dependencies
uv sync

# Run locally
uv run uvicorn backend.app.main:app --reload

# Lint & format
uv run ruff check --fix .
uv run ruff format .

# Run migrations
uv run alembic upgrade head
```
