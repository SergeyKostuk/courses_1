old_dict = {'aa': 1, 'b': 1, 'cccc': 3}
new_dict = {value: key for key, value in old_dict.items()}
print(new_dict)
