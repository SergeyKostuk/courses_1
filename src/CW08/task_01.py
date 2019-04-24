from random import randint



def create_matrix(n=randint(1, 10), random_from=1, random_to=10) -> int:
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(random_from, random_to))
        matrix.append(row)
    return matrix


matrix = create_matrix()

for row in matrix:
    print(row)
