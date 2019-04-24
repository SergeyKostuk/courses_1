def my_summ(*args):
    summ = 0
    for i, el in enumerate(args):

        summ += i * el

    return summ


a = my_summ(1, 2, 3, 4)
print(a)
