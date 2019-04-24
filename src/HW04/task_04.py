# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1
list_0 = [1, 2, 4, 5, 6, 8, 9, 2]
new_list = []
i = 1
while i <= len(list_0):
    if i == len(list_0):
        new_list.append(list_0[0])
        break
    new_list.append(list_0[i])
    i += 1
print(f'{list_0} -> {new_list}')
