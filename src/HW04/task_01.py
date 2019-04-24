#Дан список целых чисел.
#Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2
list_of_nums = [3, 5, 8, 9, 0, 67, -54, 456, -678]
i = 0
new_list = []
while i < len(list_of_nums):
    new_list.append(list_of_nums[i] * -2)
    i += 1
print(new_list)
