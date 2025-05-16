import sqlalchemy as _sql
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import sqlalchemy.ext.declarative as _declarative
from app.core import settings

engine = create_async_engine(settings.db_url)

new_async_session = async_sessionmaker(bind=engine)

Base = _declarative.declarative_base()


async def get_session():
    async with new_async_session() as session:
        yield session
