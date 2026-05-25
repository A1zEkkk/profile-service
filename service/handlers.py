from contextlib import asynccontextmanager
from repository.user import UserRepository
from service.user import UserService
from core.database.db import get_db
from core.rabbit.consumer import rabbit_consumer
from schemas.user import UserCreateSchema

async def handle_new_user_event(data):
    async with asynccontextmanager(get_db)() as session:
        repository = UserRepository(session)
        service = UserService(repository)

        user = UserCreateSchema.model_validate(data)

        await service.create_user(user)