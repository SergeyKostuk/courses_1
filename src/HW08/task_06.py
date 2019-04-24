# Дан массив целых чисел A. Найти суммы положительных и отрицательных элементов массива, используя функцию определения суммы.
def fun(*A):
    summ_of_positive = 0
    summ_of_negatives = 0
    for i in A:
        c = 'wrong input'
        if i >= 0 and not i % 1:
            summ_of_positive += i

        elif i < 0 and not i % 1:
            summ_of_negatives += i
        else:
            return c
    return summ_of_positive, summ_of_negatives


summ, summ_of_negatives = fun(3, 4, 5, -6)
print(f'summ of +: {summ}\nsumm of -:{summ_of_negatives}')
