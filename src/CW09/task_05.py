from datetime import datetime


def my_decorator(func):
    def wrap(list_a):
        for a in list_a:
            if not a % 2:
                list_a.remove(a)

        func(list_a)

    return wrap


@my_decorator
def my_func(list_a):
    for a in list_a:
        print(a)



my_func([1, 2, 3, 5])
