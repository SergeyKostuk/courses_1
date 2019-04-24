#Создать универсальны декоратор, который меняет порядок аргументов в функции на противоположный.
def my_decorator(func):
    def wrap(*args, **kwargs):
        args = args[::-1]

        a = [kwargs, args]

        return func(*a)

    return wrap
@my_decorator
def my_func(*args, **kwargs):
    print(args)
my_func(1,2,3,4,m =1,n=4)
