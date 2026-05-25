from repository.user import UserRepository, get_user_repository
from core.exc.domain.domain import AlreadyExistsError, NotFoundError, InsufficientFundsError
from schemas.user import UserResponseSchema
from fastapi import Depends


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, data):
        user = await self.repository.get_user_by_user_id(data.user_id)

        if user:
            raise AlreadyExistsError(f"User already exists with id {data.user_id}")

        result = await self.repository.create_user(data)
        return UserResponseSchema.model_validate(result)

    async def get_user(self, user_id: int)->UserResponseSchema:
        user = await self.repository.get_user_by_user_id(user_id)

        if user is None:
            raise NotFoundError(f"User with id {user_id} not found")

        return UserResponseSchema.model_validate(user)


    async def update_balance(self, data):
        user = await self.repository.get_user_by_user_id(data.user_id)

        if user is None:
            raise NotFoundError(f"User with id {data.user_id} not found")

        user = UserResponseSchema.model_validate(user)

        if user.balance + data.amount < 0:
            raise InsufficientFundsError(
                message=f"insufficient_funds_error",
                balance=user.balance,
                amount=data.amount,
            )

        update_balance = await self.repository.update_balance(data)
        return UserResponseSchema.model_validate(update_balance)


async def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository)