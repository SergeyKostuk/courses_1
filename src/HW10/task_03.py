# Имеется текстовый файл. Все четные строки этого файла записать во второй файл, а нечетные — в третий файл. Порядок следования строк сохраняется.
# Имеется текстовый файл. Переписать в другой файл все его строки с заменой в них символа 0 на символ 1 и наоборот.
def main():
    with open('test.txt') as my_file:
        lines_1 = my_file.readlines()
    with open('copy_of_odd.txt', 'w') as copy_odd:
        with open('copy_of_even.txt', 'w') as copy_even:
            i = 1
            while i < len(lines_1):
                for line in lines_1:
                    if i % 2:
                        copy_odd.write(line)
                    else:

                        copy_even.write(line)
                    i += 1

if __name__ == '__main__':
    main()
