import random
n = int(input())
m = int(input())
res = 0
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(str(random.randint(1, 9)))
    matrix.append(row)
for row in matrix:
    print(' '.join(row))
print(type(matrix[i][j]))
for row in matrix:
    for el in row:
        if int(el) == 7:
            res += 1

print(res)
