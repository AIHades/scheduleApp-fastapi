from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, Model
from models.schedule_models import *
import uvicorn


@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
    print("База данных запущена")
    yield
    print("База данных выключена")


app = FastAPI(lifespan=lifespan)


if "__main__" == __name__:
    uvicorn.run(app)