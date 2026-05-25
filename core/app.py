from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database.db import get_db, async_engine
from models import Base
from api.v1.routes import router
from .exc.base import global_app_error_handler, ApplicationError
from core.rabbit.consumer import RabbitConsumer, rabbit_consumer
from service.handlers import handle_new_user_event


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await rabbit_consumer.connect()
    await rabbit_consumer.consume("new_user", handle_new_user_event)
    yield

    await async_engine.dispose()
    await rabbit_consumer.disconnect()

def create_app()->FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.add_exception_handler(ApplicationError, global_app_error_handler)
    app.include_router(router)
    return app
