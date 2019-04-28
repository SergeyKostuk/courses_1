def max_el(matrix):
    max_el = max(matrix.data[0])
    for row in matrix.data:
        for el in row:
            if max_el < el:
                max_el = el
    return max_el


def min_el(matrix):
    min_el = min(matrix.data[0])
    for row in matrix.data:
        for el in row:
            if min_el > el:
                min_el = el
    return min_el


def summ_el(matrix):
    summa = 0
    for row in matrix.data:
        for num in row:
            summa += num
    return summa
