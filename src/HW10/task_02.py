# Имеется текстовый файл. Переписать в другой файл все его строки с заменой в них символа 0 на символ 1 и наоборот.
def main():
    with open('test.txt') as my_file:
        lines_1 = my_file.readlines()
    with open('copy_of_test.txt', 'w') as copy_txt:
        for line in lines_1:
            for i in line:
                if i == '1':
                    line = line.replace('1', '0')
                elif i == '0':
                    line = line.replace('0', '1')
            copy_txt.write(line)


if __name__ == '__main__':
    main()
