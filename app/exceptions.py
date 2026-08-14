from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request
import structlog

logger = structlog.get_logger()


# HTTP status codes
INTERNAL_SERVER_ERROR = 500
DUPLICATE_RESOURCE = 409
UNPROCESSABLE_ENTITY = 422

# core exceptions
class DuplicateResourceError(Exception):
    """Raised when attempting to create a resource that already exists."""


# Handle exceptions
async def handle_duplicate_resource_error(request: Request, exc: DuplicateResourceError):
    return JSONResponse(
        status_code= DUPLICATE_RESOURCE,
        content={
            "status_code": DUPLICATE_RESOURCE,
            "error": str(exc),
        }
    )

async def handle_internal_exception(request: Request, exc: Exception):
    logger.error("unhandled_exception", path=str(request.url), error=str(exc))
    return JSONResponse(
        status_code=INTERNAL_SERVER_ERROR,
        content={
            "status_code": INTERNAL_SERVER_ERROR,
            "error": "An unexpected error occurred. Please try again later.",
        }
    )

async def handle_unprocessable_entity_exception(request: Request, exc:RequestValidationError):
    return JSONResponse(
        status_code=UNPROCESSABLE_ENTITY,
        content={
            "status_code": UNPROCESSABLE_ENTITY,
            "error": "Invalid request data",
            "details": exc.errors(),
        }
    )



