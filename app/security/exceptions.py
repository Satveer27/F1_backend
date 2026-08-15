from app.exceptions import ResourceDoesNotExistError
from app.exceptions import AuthTokenError, ConflictLoggingIn

class InvalidTokenError(AuthTokenError):
    pass

class TokenDoesNotExist(ResourceDoesNotExistError):
    pass

class ReusingToken(AuthTokenError):
    pass

class InvalidCredentials(AuthTokenError):
    pass

class AlreadyLoggedInError(ConflictLoggingIn):
    pass