from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.db.engine import get_session

health_controller = APIRouter(prefix="/health", tags=["health"])


@health_controller.get("/")
async def health_check():
    """Basic health check endpoint"""
    return {"status": "healthy", "message": "Service is running"}


@health_controller.get("/db")
async def database_health_check(session: AsyncSession = Depends(get_session)):
    """Health check that verifies database connectivity"""
    try:
        result = await session.execute(text("SELECT 1"))
        await session.commit()
        return {"status": "healthy", "message": "Database connection successful"}
    except Exception as e:
        await session.rollback()
        return {"status": "unhealthy", "message": f"Database connection failed: {str(e)}"}
