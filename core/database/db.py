from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

dns_db = "postgresql+asyncpg://postgres:password@localhost:5432/postgres"

async_engine = create_async_engine(url=dns_db, echo=True)
async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_db():
    async with async_session() as session:
        async with session.begin():
            yield session

