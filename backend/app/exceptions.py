from fastapi import status


class BaseAppError(Exception):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail: str = "Internal server error"

    def __init__(self, detail: str | None = None):
        self.detail = detail or self.__class__.detail
        super().__init__(self.detail)


class NotFoundError(BaseAppError):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Resource not found"


class AlreadyExistsError(BaseAppError):
    status_code = status.HTTP_409_CONFLICT
    detail = "Resource already exists"


class ForbiddenError(BaseAppError):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Access denied"


class BadRequestError(BaseAppError):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad request"


class UnauthorizedError(BaseAppError):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Not authenticated"
