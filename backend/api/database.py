from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_CONFIG = "postgresql+asyncpg://postgres:100pregetup-nst@localhost:5432/postgres"
Base = declarative_base()

class AsyncDatabaseSession:
    def __init__(self):
        self.session = None
        self.engine = None

    def __getattr__(self, name):
        if not self.session:
            raise AttributeError(f"Session is not initialized. Call `init()` before using the database.")
        return getattr(self.session, name)

    def init(self):
        if not self.engine:
            self.engine = create_async_engine(DB_CONFIG, future=True, echo=True, pool_size=10, max_overflow=20)
        if not self.session:
            self.session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)()

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


db = AsyncDatabaseSession()
db.init()  # Certifica-te de que o init é chamado em algum lugar antes de usar db

async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
