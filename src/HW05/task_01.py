# Дана целочисленная матрица размера 5х5. Получить новую матрицу
# путем деления всех элементов данной матрицы на ее наибольший по
# модулю элемент.
max_el = 0
matrix_2 = []
matrix_1 = [
    [-64, -5, -65, -7, -8],
    [-4, -5, -3, -9, -13],
    [-7, -18, -5, -1, -2],
    [-6, -50, -34, -16, -21],
    [-33, 58, 6, -7, -12],
]
for i in range(5):
    row = matrix_1[i]
    for j in range(5):
        if abs(row[j]) > max_el:
            max_el = abs(row[j])
print(f'max element -> {max_el}')
if not max_el:
    print('null matrix')
else:
    for i in range(5):
        row_2 = []
        for j in range(5):
            row_2.append(str(matrix_1[i][j] / max_el))
        matrix_2.append(row_2)
    for row_2 in matrix_2:
        print(' '.join(row_2))
