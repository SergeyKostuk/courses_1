#Дан список целых чисел. Подсчитать сколько четных чисел в списке'

list_of_nums = [3, 5, 8, 9, 0, 67, -54, 456, -678, 44, 66]
res = 0
i = 0
while i < len(list_of_nums):
    #if list_of_nums[i] % 2 == 0:
    if not list_of_nums[i] % 2:
        res += 1
    i += 1
print(f'number of even elements is {res}')
