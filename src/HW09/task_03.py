def my_decorator(func):
    def wrap(list_a):
        i = 0
        while i < len(list_a):
            if list_a[i] % 2 == 0:
                list_a.remove(list_a[i])
                i = i -1
            i += 1
        return func(list_a)

    return wrap


@my_decorator
def my_func(list_a):
    for a in list_a:
        print(a)


my_func([1, 2, 3, 5, 6, 11, 4, 20, 7, 8])


#Создать декоратор для функции, которая принимает список чисел. Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.