from app.users.repository import UserRepository
from fastapi import Depends
from app.database import get_db
from app.users.service import UserService
from sqlalchemy.ext.asyncio import AsyncSession

def create_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def create_user_service(user_repository: UserRepository = Depends(create_user_repository)) -> UserService:
    return UserService(user_repository)