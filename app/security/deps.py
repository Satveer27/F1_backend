from app.security.repository import RefreshTokenRepository
from fastapi import Depends
from app.core.database.database import get_db
from app.security.service import JWTService
from sqlalchemy.ext.asyncio import AsyncSession
from app.users.repository import UserRepository
from app.users.deps import create_user_repository

def create_refresh_token_repository(db: AsyncSession = Depends(get_db)) -> RefreshTokenRepository:
    return RefreshTokenRepository(db)

def create_jwt_service(refresh_token_repository: RefreshTokenRepository = Depends(create_refresh_token_repository), 
                       user_repository: UserRepository = Depends(create_user_repository)) -> JWTService:
    return JWTService(refresh_token_repository, user_repository)