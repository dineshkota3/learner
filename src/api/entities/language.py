from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.api.entities.base import Base, TimestampMixin


class Language(Base, TimestampMixin):
    """Language entity for storing programming languages"""

    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    language: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"<Language(id={self.id}, language={self.language})>"
