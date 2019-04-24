import random
n = int(input())
m = int(input())
sredn = 0
summa = 0
matrix = []
g = 0
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1, 9))
    matrix.append(row)
for row in matrix:
    for el in row:
        summa += el
sredn = summa / (n*m)


for i, row_1 in enumerate(matrix):
    for j, el in enumerate(row):
        if not ((j + i) % 2) and el > sredn:
            print(el)
            print(f'{i} {j}')





# for row in matrix:
#     for el in row:
#         if el > sredn:
#             print(el)

for row in matrix:
    print(row)
print(sredn)