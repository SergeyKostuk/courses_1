#Составить список чисел Фибоначчи содержащий 15 элементов.
list_of_nums = [0, 1]
while len(list_of_nums) < 15:
    list_of_nums.append(list_of_nums[-1] + list_of_nums[-2])
print(list_of_nums)
