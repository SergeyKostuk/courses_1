# Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε — вещественные, ε > 0), находящую приближенное значение функции sin( x ):
# sin( x ) = x – x 3 /(3!) + x 5 /(5!) – ... + (–1) n · x 2·n+1 /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые, модуль которых больше ε . С помощью Sin1 найти приближенное значение синуса для данного x при шести данных ε .  [01-11.3-Proc41]
from typing import Union
from math import pi
def Sin1(x, ε: Union[int, float]):
    x = x % (2 * pi)
    if ε < 0:
        er = 'wrong input'
        return er
    else:

        intermediate = ε
        sin_x = 0
        i = 1
        fact = 1
        j = 0
        X = x
        while abs(intermediate) >= ε:
            intermediate = (((-1) ** j) * X / fact)
            fact *= (i + 1) * (i + 2)
            X *= x * x
            sin_x += intermediate
            i += 2
            j += 1
        return sin_x


angle = 0.009
a = [-0.2, 0.5, 0.002, 0.2, 0.5, 0.002]
for i in a:
    print(f'with ε = {i} -> sin({angle}) = {Sin1(angle, i)}\n')
