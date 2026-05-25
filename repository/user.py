from fastapi import Depends
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from core.database.db import get_db
from models.user import User
from decimal import Decimal

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, data):
        stmt = insert(User).values(**data.model_dump()).returning(User)
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def get_user_by_user_id(self, user_id):
        stmt = select(User).where(User.user_id == user_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def update_balance(self, data):
        stmt = update(User).where(User.user_id == data.user_id).values(balance=User.balance + data.amount).returning(User)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()


async def get_user_repository(db: AsyncSession = Depends(get_db)) ->UserRepository:
    return UserRepository(db)