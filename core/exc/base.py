from fastapi import Request
from fastapi.responses import JSONResponse

class ApplicationError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


async def global_app_error_handler(request: Request, exc: ApplicationError):
    return JSONResponse(
        status_code=getattr(exc, "status_code", 400),
        content={
            "success": False,
            "error": {
                "type": getattr(exc, "error_type", "application_error"),
                "message": exc.message,
                "details": getattr(exc, "details", None)
            }
        }
    )