import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.config import settings
from api_v1 import router as router_v1
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
async def index():
    return "Hello World!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
