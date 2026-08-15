from app.users.repository import UserRepository
from app.users.schemas import UserCreateSchema
from app.users.exceptions import UserAlreadyExistsError
from app.users.schemas import UserResponseSchema
from app.users.models import User
from app.security.utils.password import hash_password

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user_service(self, request: UserCreateSchema):
        exists = await self.user_repository.get_user_by_email(request.email)
        if exists:
            raise UserAlreadyExistsError(f"User with email {request.email} already exists.")

        hashed_password = hash_password(request.password)

        user = User(
            email = request.email,
            username = request.username,
            password = hashed_password,
            f1_team = request.f1_team
        )

        result = await self.user_repository.create_user(user)

        return UserResponseSchema.model_validate(result)
        
        