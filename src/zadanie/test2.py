class RO():
    def __init__(self):
        self.matrix1 = []

    def C(self, w, h):

        matrix = []
        for i in range(h + 2):
            row = []
            for j in range(w + 2):
                if i == 0 or i == h + 1:

                    row.append('-')
                elif j == 0 or j == w + 1:
                    row.append('|')
                else:
                    row.append(' ')
            matrix.append(row)

        return matrix

    def L(self, x1, y1, x2, y2, matrix):
        lenght_1 = x2 - x1
        lenght_2 = y2 - y1
        if not lenght_2:
            for i in range(lenght_1 + 1):
                matrix[y1][x1 + i] = 'x'
        elif not lenght_1:
            for i in range(lenght_2 + 1):
                matrix[y1 + i][x1] = 'x'

    def R(self, x1, y1, x2, y2, matrix):
        lenght_1 = x2 - x1
        lenght_2 = y2 - y1

        for i in range(lenght_1 + 1):
            matrix[y1][x1 + i] = 'x'
            matrix[y2][x1 + i] = 'x'

        for i in range(lenght_2 + 1):
            matrix[y1 + i][x1] = 'x'
            matrix[y1 + i][x2] = 'x'

    def B(self, x, y, char, matrix):
        if (x > 0 and x < len(matrix[0]) - 1 and y > 0 and y < len(matrix) - 1):
            if (matrix[y][x] == ' '):
                matrix[y][x] = char

                self.B(x, y + 1, char, matrix)
                self.B(x + 1, y, char, matrix)
                self.B(x - 1, y, char, matrix)
                self.B(x, y - 1, char, matrix)


    def write_in_file(self, matrix):
        with open('output.txt', 'a') as my_file:
            for row in matrix:
                line = ''.join(map(str, row))
                my_file.write(f'{line}\n')

    def run(self):
        with open('input.txt') as my_file:
            lines_1 = my_file.readlines()
            a = []
            for line in lines_1:
                a.append(line.split())
            for el in a:
                if el[0] != 'B':
                    coord = list(map(int, el[1:]))
                b = RO()

                if el[0] == 'C':
                    m = b.C(coord[0], coord[1])
                    b.write_in_file(m)
                elif el[0] == 'L':
                    b.L(coord[0], coord[1], coord[2], coord[3], m)
                    b.write_in_file(m)
                elif el[0] == 'R':
                    b.R(coord[0], coord[1], coord[2], coord[3], m)
                    b.write_in_file(m)
                elif el[0] == 'B':
                    b.B(int(el[1]), int(el[2]), el[3], m)
                    b.write_in_file(m)
def main():


    a = RO()
    a.run()


if __name__ == '__main__':
    main()
