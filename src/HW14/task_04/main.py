from classes import Math, ComplexMath
from ui import start_1, start_2
from exceptions import IncorrectInputError, NoSpaces


def main():
    while True:

        start_1()
        try:
            desision_0 = int(input('u desision is? '))
        except ValueError:
            print('chose 1 or 2')
        if desision_0 != 1 or desision_0 != 2:
            print('only one or two')
        start_2()
        if desision_0 == 1:
            continue
            desision = input('Write your desision sir : ')
            try:
                desision = int(desision)
            except ValueError as err:
                print(f'{err}')
                continue
            if not desision:
                print('See you next time sir')
                break
            elif desision > 4:
                print('check list of comands again, sir')
                continue

            try:
                real_1 = float(input('real of first num: '))
                imag_1 = float(input('imaginary of first num: '))
                real_2 = float(input('real of second num: '))
                imag_2 = float(input('imaginary of second num: '))
                a = ComplexMath(real_1, imag_1, real_2, imag_2)
            except ValueError:
                print('only nums')
            else:
                if desision == 1:

                    a.summ()
                elif desision == 2:

                    a.diff()
                elif desision == 3:

                    a.mult()
                elif desision == 4:

                    try:

                        a.division()
                    except ZeroDivisionError as err:

                        print(err)

        if desision_0 == 2:
            desision = input('Write your desision sir : ')
            try:
                desision = int(desision)
            except ValueError as err:
                print(f'{err}')
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
                a = Math(arg_1, arg_2)
            except NoSpaces as err:
                print(f'{err}')
            except IncorrectInputError as err:
                print(f'{err}')
            else:
                if desision == 1:

                    a.summ()
                elif desision == 2:

                    a.diff()
                elif desision == 3:

                    a.mult()
                elif desision == 4:

                    try:

                        a.division()
                    except ZeroDivisionError as err:

                        print(f'second num  is zero - {err}!!!')


if __name__ == "__main__":
    main()
