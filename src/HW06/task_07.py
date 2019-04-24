# Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.
import random
n = int(input())
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(1, 40))
    matrix.append(row)
for row in matrix:
    print(row)
for i in range(n):
    max_el = 0
    for j in range(n):
        if matrix[i][j] > max_el:
            max_el = matrix[i][j]
            ind_of_mel_1 = i
            ind_of_mel_2 = j
    middle_el = matrix[i][i]
    matrix[i][i] = max_el
    matrix[ind_of_mel_1][ind_of_mel_2] = middle_el
print()
for row in matrix:
    print(row)
print(matrix[1][2])