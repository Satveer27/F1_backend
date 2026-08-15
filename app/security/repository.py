from sqlalchemy.ext.asyncio import AsyncSession
from app.security.models import RefreshToken
from sqlalchemy import select
from uuid import UUID

class RefreshTokenRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_refresh_token(self, refresh_token: RefreshToken)-> RefreshToken:
        self.db.add(refresh_token)
        await self.db.commit()
        await self.db.refresh(refresh_token)

        return refresh_token

    async def update_refresh_token(self, refresh_token: RefreshToken) -> RefreshToken:
        self.db.add(refresh_token)
        await self.db.commit()
        await self.db.refresh(refresh_token)
        return refresh_token

    async def delete_refresh_token(self, refresh_token: RefreshToken):
        await self.db.delete(refresh_token)
        await self.db.commit()

    async def get_refresh_token_by_jti(self, refresh_id: UUID) -> RefreshToken | None:
        result =  await self.db.execute(select(RefreshToken).where(RefreshToken.jti == refresh_id))
        return result.scalar_one_or_none()

    async def get_refresh_token_by_user_id(self, user_id: UUID) -> list[RefreshToken]:
            result =  await self.db.execute(select(RefreshToken).where(RefreshToken.user_id == user_id))
            return list(result.scalars().all())
            