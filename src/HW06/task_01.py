# 1) Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
# Вычислить результат Z в зависимости от знака. Предусмотреть реакции на возможный неверный знак операции, а также на ввод Y=0 при делении.
#     Организовать возможность многократных вычислений без перезагрузки программа (т.е. построить бесконечный цикл).
# В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').
Z = 0
possible_opirations = ['+', '-', '/', '*']
while True:
    X = float(input("X: \n"))
    Y = float(input("Y: \n"))
    sign = input(f'possible operations are: {" ".join(possible_opirations)}\npress 0 for QUIT:\n')
    if sign in possible_opirations:
        if sign == possible_opirations[0]:
            Z = X + Y
            print(Z)
        elif sign == possible_opirations[1]:
            Z = X - Y
            print(Z)
        elif sign == possible_opirations[2]:
            if Y == 0:
                print('division by 0')
                continue
            Z = X / Y
            print(Z)
        elif sign == possible_opirations[3]:
            Z = X * Y
            print(Z)
        else:
            print('wrong input')
    if sign not in possible_opirations and sign != '0':
        print('wrong input')
    else:
        break
