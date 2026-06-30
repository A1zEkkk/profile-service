from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from core.config import get_settings

settings = get_settings()

async_engine = create_async_engine(url=settings.database_url, echo=True)
async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_db():
    """
    С автокоммитами из-за того, что у нас бегин
    """
    async with async_session() as session:
        async with session.begin():
            yield session

