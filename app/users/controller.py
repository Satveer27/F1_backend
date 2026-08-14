from app.users.schemas import UserResponseSchema, UserCreateSchema
from app.users.deps import create_user_service
from fastapi import Depends
from app.users.service import UserService
from fastapi import APIRouter

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.post("/signup", response_model=UserResponseSchema, status_code=201)
async def signup(payload: UserCreateSchema, service : UserService = Depends(create_user_service)):
    return await service.create_user_service(payload)