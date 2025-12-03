import asyncio
from logging.config import fileConfig

from alembic import context
import models.user
import models.task
from core.database import engine

config = context.config
fileConfig(config.config_file_name)
target_metadata = models.user.Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

async def do_run_migrations(connection):
    await connection.run_sync(lambda conn: context.configure(connection=conn, target_metadata=target_metadata))
    await connection.run_sync(lambda conn: context.run_migrations())

def run_migrations_online():
    async def main():
        async with engine.begin() as conn:
            await conn.run_sync(lambda sync_conn: context.configure(connection=sync_conn, target_metadata=target_metadata))
            await conn.run_sync(lambda sync_conn: context.run_migrations())
    asyncio.run(main())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
