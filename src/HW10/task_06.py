# Дан файл, содержащий различные даты. Каждая дата - это число, месяц и год. Найти самую раннюю дату. [02-8.1-ML-29]
from datetime import date


def main():
    with open('task_06.txt') as my_file:
        lines_1 = my_file.readlines()
        list_of_dates = []

        for i in lines_1:
            one_date = list(map(int, i.split(':')))
            datetime_format = date(*one_date[::-1])
            list_of_dates.append(datetime_format)

        print(min(list_of_dates))


if __name__ == '__main__':
    main()
