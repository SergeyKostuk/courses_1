from typing import Union


def my_calculation(x: Union[int, float]) -> float:
    addend = (x ** 0.5 + x) / 2
    return addend


res = my_calculation(5) + my_calculation(12) + my_calculation(19)
print(res)
