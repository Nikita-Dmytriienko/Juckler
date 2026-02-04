import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_health(client: AsyncClient):
    response = await client.get("/health/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


async def test_root(client: AsyncClient):
    response = await client.get("/health/")
    assert response.status_code == 200


async def test_register(client: AsyncClient):
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "newuser@test.com",
            "username": "newuser",
            "password": "strongpass123",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "newuser@test.com"
    assert data["username"] == "newuser"
    assert data["is_active"] is True
    assert "id" in data


async def test_register_duplicate_email(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "dup@test.com",
            "username": "dupuser1",
            "password": "strongpass123",
        },
    )
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "dup@test.com",
            "username": "dupuser2",
            "password": "strongpass123",
        },
    )
    assert response.status_code == 400


async def test_login(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "logintest@test.com",
            "username": "loginuser",
            "password": "strongpass123",
        },
    )
    response = await client.post(
        "/api/v1/auth/jwt/login",
        data={"username": "logintest@test.com", "password": "strongpass123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


async def test_login_wrong_password(client: AsyncClient):
    response = await client.post(
        "/api/v1/auth/jwt/login",
        data={"username": "logintest@test.com", "password": "wrongpassword"},
    )
    assert response.status_code == 400


async def test_me_authenticated(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "metest@test.com",
            "username": "meuser",
            "password": "strongpass123",
        },
    )
    login = await client.post(
        "/api/v1/auth/jwt/login",
        data={"username": "metest@test.com", "password": "strongpass123"},
    )
    token = login.json()["access_token"]

    response = await client.get(
        "/api/v1/auth/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "metest@test.com"
    assert data["username"] == "meuser"


async def test_me_unauthenticated(client: AsyncClient):
    response = await client.get("/api/v1/auth/users/me")
    assert response.status_code == 401
