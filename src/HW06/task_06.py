# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число больше предыдущего)
#
import random
import datetime
n = int(input())
print(datetime.datetime.now())
num_list = [random.randint(-5, 4) for i in range(n)]
i = -1
res = 0
print(num_list)
while i > -len(num_list):
    if num_list[i] > num_list[i - 1]:
        if i - 1 == -len(num_list):
            res += 1
            break
        i -= 1
    else:
        num_list = num_list[:i]
        if i != -1:
            res += 1
        i = -1

print(res)
print(datetime.datetime.now())