class IncorrectInputError(Exception):
    def __init__(self, message='only nums sir'):
        super().__init__(message)


class NoSpaces(Exception):
    def __init__(self, message='no spaces sir'):
        super().__init__(message)
