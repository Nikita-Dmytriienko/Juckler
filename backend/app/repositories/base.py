from typing import Generic, TypeVar
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)

#BASE REPOSITORY
class BaseRepository(Generic[ModelType]):
    def __init__(self, model: type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    # GET ALL
    async def get_all(self,*,skip: int = 0, limit: int = 100,) -> list[ModelType]:
            query = select(self.model).offset(skip).limit(limit)
            result = await self.session.execute(query)
            return list(result.scalars().all())

    # GET BY ID
    async def get_by_id(self, id: UUID) -> ModelType | None:
        return await self.session.get(self.model, id)

    # CREATE
    async def create(self, object: ModelType) -> ModelType:
        self.session.add(object)
        await self.session.flush()
        await self.session.refresh(object)
        return object

    # UPDATE
    async def update(self, object: ModelType) -> ModelType:
        await self.session.flush()
        await self.session.refresh(object)
        return object

    # DELETE
    async def delete(self, object: ModelType) -> None:
        await self.session.delete(object)
        await self.session.flush()

    # COUNT
    async def count(self) -> int:
        query = select(func.count()).select_from(self.model)
        result = await self.session.execute(query)
        return result.scalar_one()
