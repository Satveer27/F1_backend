from fastapi import Depends
from app.core.database.database import asyncSessionMaker
import structlog
from app.security.repository import RefreshTokenRepository
from app.security.deps import create_refresh_token_repository

logger = structlog.get_logger()

async def clean_refresh_tokens():
    async with asyncSessionMaker() as db:
        repository = RefreshTokenRepository(db)
        deleted_count = await repository.cleanup_expired_refresh_tokens()
        print("log done via")
        logger.info("expired_refresh_tokens_cleaned", count=deleted_count)




   