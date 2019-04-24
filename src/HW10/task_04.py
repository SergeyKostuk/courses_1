# Имеются два текстовых файла с одинаковым числом строк. Выяснить, совпадают ли их строки. Если нет, то получить номер первой строки, в которой эти файлы отличаются друг от друга.[03-15.31]
def main():
    with open('task_4_1.txt') as my_1_file:
        with open('task_4_2.txt') as my_2_file:
            lines_1 = my_1_file.readlines()
            lines_2 = my_2_file.readlines()
            i = 0
            while i < len(lines_2):
                if lines_2[i] != lines_1[i]:
                    c = f'differences in {i+1} line'
                    return c
                i += 1


if __name__ == '__main__':
    print(main())
