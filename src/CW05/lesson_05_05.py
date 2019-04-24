import random
n = int(input())
res = 0
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(str(random.randint(1, 9)))
    matrix.append(row)
for row in matrix:
    print(' '.join(row))
print(type(matrix[i][j]))
for row in matrix:
    for el in row:
        if int(el) % 3 == 0:
            res += int(el)

print(res)
