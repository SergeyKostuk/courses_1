# Описать функцию is_power_n( k , n ) логического типа, возвращающую True, если целый параметр k (> 0) является степенью числа n (> 1), и False в противном случае.
# Дано число n (> 1) и набор из 10 целых положительных чисел. С помощью функции is_power_n найти количество степеней числа N в данном наборе.[01-11.2-Proc17]
#
#
from math import log


def is_power_n(k, n):
    if n > 1 and k > 0:
        k_pow = (log(k, n))
        if not k_pow % 1:
            return True
        else:
            return False
    else:
        return 'error'


print(is_power_n(3, 2))
a = [3, 4, 6, 8, -1, -14]
for i in a:
    print(is_power_n(i, 2))
