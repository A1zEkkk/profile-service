from starlette import status
from decimal import Decimal

from .base import DomainError

class AlreadyExistsError(DomainError):
    status_code: int = status.HTTP_409_CONFLICT

    def __init__(self, message: str = "already_exists_error"):
        super().__init__(message)


class NotFoundError(DomainError):
    status_code: int = status.HTTP_404_NOT_FOUND

    def __init__(self, message: str = "not_found_error"):
        super().__init__(message)


class InsufficientFundsError(DomainError):
    status_code: int = status.HTTP_400_BAD_REQUEST

    def __init__(self, *, balance: Decimal, amount: Decimal, message: str = "insufficient_funds_error"):
        self.balance = balance
        self.amount = amount
        super().__init__(message)