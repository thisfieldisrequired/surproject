import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.models import Base, db_helper

from users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)


@app.get("/")
async def index():
    return "Hello World!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
