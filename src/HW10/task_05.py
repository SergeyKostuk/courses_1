# Создать матрицу случайных чисел и сохранить ее в json файл. После прочесть ее, обнулить все четные элементы и сохранить в другой файл
import json
from random import randint


def create_matrix(n):
    matrix = [[randint(1, 9) for j in range(n)] for i in range(n)]
    return matrix


def save_in_file(matrix):
    with open('source_matrix.txt', 'w') as my_file:
        data = json.dumps(matrix)
        my_file.write(data)


def lol():
    with open('source_matrix.txt') as my_file_1:
        with open('changed_matrix.txt', 'w') as my_file_2:
            matrix = json.loads(my_file_1.read())

            n = len(matrix)
            for i in range(n):
                for j in range(n):
                    if not matrix[i][j] % 2:
                        matrix[i][j] = 0

            data = json.dumps(matrix)
            my_file_2.write(data)


def main():
    save_in_file(create_matrix(4))
    lol()


if __name__ == '__main__':
    main()
