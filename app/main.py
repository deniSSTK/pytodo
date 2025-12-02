from fastapi import FastAPI

from routers import user, auth
from core.database import Base, engine

import models.user
import models.task

app = FastAPI(title="TaskManager")

app.include_router(user.router)
app.include_router(auth.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(lambda sync_conn: Base.metadata.create_all(bind=sync_conn))
