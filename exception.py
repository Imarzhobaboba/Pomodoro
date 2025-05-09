class UserNotFoundException(Exception):
    detail = 'user not found'

class UserNotCorrectPasswordException(Exception):
    detail = 'incorrect password'

class TokenExpired(Exception):
    detail = 'token has expired'

class TokenNotCorrect(Exception):
    detail = 'token is incorrect'

class TaskNotFound(Exception):
    detail = 'task not found'