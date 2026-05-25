from fastapi import status
from core.exc.base import ApplicationError
from typing import Optional, Dict, Any

class DomainError(ApplicationError):
    status_code: int = status.HTTP_400_BAD_REQUEST
    error_type: str = "domain_error"

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        self.details = details
        super().__init__(message)