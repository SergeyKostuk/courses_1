#В массиве целых чисел с количеством элементов 19 определить максимальное число и заменить им все четные по значению элементы
import random
array_of_nums = [random.randint(-50, -10) for i in range(19)]
max_num = array_of_nums[0]
print(array_of_nums)
i = 0
for el in array_of_nums:
    if el > max_num:
        max_num = el
while i < 19:
    if not array_of_nums[i] % 2:
        array_of_nums[i] = max_num
    i += 1
print(array_of_nums)
