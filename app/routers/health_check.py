from fastapi import APIRouter
from fastapi import HTTPException, status
from sqlalchemy import text

from app.db.postgres_db import engine

router = APIRouter(tags=["Health check"])


@router.get("/", status_code=status.HTTP_200_OK)
def health_check():
    return {
        "status_code": status.HTTP_200_OK,
        "detail": "ok",
        "result": "working"
    }


@router.get("/health/db")
async def check_db_health():
    try:
        async with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))
        return {"status": "Database Postgres is healthy"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Postgres connection error: {ex}")

