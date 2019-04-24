# Создать универсальны декоратор, который меняет порядок аргументов в функции на противоположный.
def my_decorator(func):
    def wrap(a, b, c):
        a = [a, b, c
             ]

        func(*a[::-1])

    return wrap


@my_decorator
def my_func(a, b, c ):
    print(a + b * c)


my_func(1, 2, 3)
