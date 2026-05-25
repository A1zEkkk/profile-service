from fastapi import Depends, APIRouter
from schemas.user import UserCreateSchema, UserResponseSchema, UserUpdateSchema
from service.user import UserService, get_user_service

router = APIRouter()


@router.post(
    "/create",
    response_model=UserResponseSchema,
)
async def create_user(user: UserCreateSchema, service: UserService = Depends(get_user_service)):
    return await service.create_user(user)

@router.get("/get_user/{user_id}")
async def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return await service.get_user(user_id)

@router.put(
    "/update_balance",
    response_model=UserResponseSchema
)
async def update_balance(user_data: UserUpdateSchema, service: UserService = Depends(get_user_service)):
    return await service.update_balance(user_data)