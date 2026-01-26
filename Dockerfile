FROM python:3.13

WORKDIR /app

# uv set
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# copy pyproject.toml and lock
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache

# copy code
COPY . .

EXPOSE 8000

# Deploy
CMD ["uv", "run", "uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]