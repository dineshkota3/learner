from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.db.engine import get_session
from src.api.services.language_service import LanguageService
from src.api.entities.language import Language


# Pydantic models for request/response
class LanguageResponse(BaseModel):
    """Response model for language"""
    id: int
    language: str

    class Config:
        from_attributes = True


class LanguageCreate(BaseModel):
    """Request model for creating a language"""
    language: str = Field(..., min_length=1, max_length=255)


# Router
language_controller = APIRouter(prefix="/languages", tags=["languages"])


@language_controller.get("", response_model=List[LanguageResponse])
async def get_languages(session: AsyncSession = Depends(get_session)):
    """Get all languages"""
    languages = await LanguageService.get_all_languages(session)
    return languages


@language_controller.get("/{language_id}", response_model=LanguageResponse)
async def get_language(language_id: int, session: AsyncSession = Depends(get_session)):
    """Get a language by ID"""
    language = await LanguageService.get_language_by_id(session, language_id)
    if not language:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Language with id {language_id} not found"
        )
    return language


@language_controller.post("", response_model=LanguageResponse, status_code=status.HTTP_201_CREATED)
async def create_language(language_data: LanguageCreate, session: AsyncSession = Depends(get_session)):
    """Create a new language"""
    # Check if language already exists
    if await LanguageService.language_exists(session, language_data.language):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Language '{language_data.language}' already exists"
        )

    language = await LanguageService.create_language(session, language_data.language)
    await session.commit()
    return language
