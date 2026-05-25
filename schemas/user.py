from pydantic import BaseModel, ConfigDict
from decimal import Decimal

class UserCreateSchema(BaseModel):
    user_id: int
    name: str
    surname: str
    phone: str

class UserResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    name: str
    surname: str
    phone: str
    balance: Decimal

class UserUpdateSchema(BaseModel):
    user_id: int
    amount: Decimal
