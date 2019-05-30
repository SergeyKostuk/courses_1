def create_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            if i == 0 or i == n - 1:

                row.append('-')
            elif j == 0 or j == m - 1:
                row.append('|')
            else:
                row.append(' ')
        matrix.append(row)
    with open('output.txt', 'a') as my_file:
        for row in matrix:
            line = ''.join(map(str, row))
            my_file.write(f'{line}\n')
def main():
    with open('input.txt') as my_file:
        lines_1 = my_file.readlines()
        a=[]
        for line in lines_1:
            a.append(line.split())

    print(lines_1)
    print(a)


if __name__ == '__main__':
    main()
