import random
n = int(input())
res = 0
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(1, 9))
    matrix.append(row)
for row in matrix:
    print(row)
print(type(matrix[i][j]))
for i in range(n):
    for j in range(n):
        if not matrix[i][j] % 3:
            res += matrix[i][j]

print(res)
