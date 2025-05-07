class UserNotFoundException(Exception):
    detail = 'user not found'

class UserNotCorrectPasswordException(Exception):
    detail = 'incorrect password'