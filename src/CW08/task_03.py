from random import randint
def my_summ(*args):

    return sum(args), max(args)


summa, max_el = my_summ(*[1, 4, 5, 7, 10])
print(f'total = {summa}, biggest element = {max_el}')

