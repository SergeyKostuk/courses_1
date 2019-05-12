from exceptions import IncorrectInputError, NoSpaces


def summ(num_1, num_2):
    return(float(num_1) + float(num_2))


def diff(num_1, num_2):
    return(float(num_1) - float(num_2))


def mult(num_1, num_2):
    return(float(num_1) * float(num_2))


def division(num_1, num_2):
    return(float(num_1) / float(num_2))


def valid(arg_1, arg_2):
    if not arg_1.lstrip('-').isdigit() or not arg_2.lstrip('-').isdigit() :
        raise IncorrectInputError()
def valid_2(arg_1, arg_2):
    if len(arg_1.split()) > 1 or len(arg_2.split()) > 1:
        raise NoSpaces()
