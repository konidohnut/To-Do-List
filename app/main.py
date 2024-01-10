from fastapi import FastAPI
import uvicorn

from app.core.config import settings
from app.routers import health_check, tasks
from app.logger import get_logger

app = FastAPI(title="FastAPI, Docker, Postgres")

logger = get_logger()

app.include_router(health_check.router)
app.include_router(tasks.router)


if __name__ == '__main__':
    uvicorn.run("app.main:app", host=settings.fast_api_host, port=settings.fast_api_port, reload=True)
