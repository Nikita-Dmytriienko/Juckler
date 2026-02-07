from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.models.category import Category, CategoryType
from backend.app.repositories.base import BaseRepository

class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: AsyncSession):
        super().__init__(Category,session)

    # GET BY USER
    async def get_by_user(self,
                          user_id: UUID,
                          *,
                          category_type:CategoryType | None = None,
                          skip: int = 0,
                          limit: int = 100,
    ) -> list[Category]:
        query = select(Category).where(Category.user_id == user_id)
        if category_type:
            query = query.where(Category.type == category_type)


        query = query.offset(skip).limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    # GET BY NAME AND USER
    async def get_by_name_and_user(self,
                                   name: str,
                                   user_id: UUID,
                                   ) -> Category | None:
        query = select(Category).where(Category.name == name,
                                       Category.user_id == user_id,
        )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    # GET COUNT BY USER
    async def count_by_user(self,
                            user_id: UUID) -> int:
        query = select(
            func.count()).where(Category.user_id == user_id
        )
        result = await self.session.execute(query)
        return result.scalar_one()