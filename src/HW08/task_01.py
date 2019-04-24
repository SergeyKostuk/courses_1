# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое. Написать программу в виде трех функций.
#
#
def arifm(*args):
    summa = 0
    for el in args:
        summa += el
    average_A = summa / len(args)
    return average_A


def geometr(*args):
    mult = 1
    for el in args:
        mult *= el
    average_G = mult ** (1 / len(args))
    return average_G


def func(mean_type, *args):
    if mean_type == 'arif':
        return arifm(*args)
    elif mean_type == 'geom':
        return geometr(*args)
    else:
        mistake = 'wrong comand'
        return mistake


print(func('arif', 1, 2, 3))
print(func('geom', 1, 2, 3))
print(func('blabla', 1, 2, 3))
