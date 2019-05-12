import random


def create_matrix(n=4):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(1, 40))
        matrix.append(row)
    return matrix


def print_matrix(martix):
    for row in martix:
        for el in row:
            print(el, end=' ')
        print()


def summ_el(matrix):
    summa = 0
    for row in matrix:
        for num in row:
            summa += num
    return summa


def max_el(matrix):
    max_el = max(matrix.data[0])
    for row in matrix.data:
        for el in row:
            if max_el < el:
                max_el = el
    return max_el


def min_el(matrix):
    min_el = min(matrix[0])
    for row in matrix:
        for el in row:
            if min_el > el:
                min_el = el
    return min_el


g = create_matrix()
print_matrix(g)
summa_elemntov = summ_el(g)
print(f'sum of els --->{summa_elemntov}')
print(f'biggest el in matrix ---> {max_el(g)}')
print(f'smallest el of matrix ---> {min_el(g)}')
