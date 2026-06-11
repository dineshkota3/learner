from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from src.api.entities.language import Language


class LanguageService:
    """Service for handling language-related business logic"""

    @staticmethod
    async def get_all_languages(session: AsyncSession) -> List[Language]:
        """Get all languages"""
        result = await session.execute(select(Language).order_by(Language.id))
        return list(result.scalars().all())

    @staticmethod
    async def get_language_by_id(session: AsyncSession, language_id: int) -> Language | None:
        """Get a language by ID"""
        result = await session.execute(select(Language).where(Language.id == language_id))
        return result.scalars().first()

    @staticmethod
    async def create_language(session: AsyncSession, language_name: str) -> Language:
        """Create a new language"""
        language = Language(language=language_name)
        session.add(language)
        await session.flush()
        await session.refresh(language)
        return language

    @staticmethod
    async def language_exists(session: AsyncSession, language_name: str) -> bool:
        """Check if a language already exists"""
        result = await session.execute(
            select(Language).where(Language.language == language_name)
        )
        return result.scalars().first() is not None
