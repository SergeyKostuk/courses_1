from func import valid, summ, valid_2, diff, mult, division
from ui import start
from exceptions import IncorrectInputError, NoSpaces


def main():
    while True:

        start()
        desision = input('Write your desision sir : ')
        try:
            desision = int(desision)
        except ValueError:
            print('u should wrine number of comand sir')
            continue
        if not desision:
            print('See you next time sir')
            break
        elif desision > 4:
            print('check list of comands again, sir')
            continue

        try:
            arg_1 = input('first arg: ')
            arg_2 = input('second arg: ')
            valid_2(arg_1, arg_2)
            valid(arg_1, arg_2)
        except NoSpaces as err:
            print(f'{err}')
        except IncorrectInputError as err:
            print(f'{err}')
        else:
            if desision == 1:

                summ(arg_2, arg_1)
            elif desision == 2:

                diff(arg_1, arg_2)
            elif desision == 3:

                mult(arg_1, arg_2)
            elif desision == 4:

                try:

                    division(arg_1, arg_2)
                except ZeroDivisionError as err:

                    print(f'second num  is zero - {err}!!!')


if __name__ == "__main__":
    main()
