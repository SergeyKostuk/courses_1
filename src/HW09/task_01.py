# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i это порядковый номер строки в списке. Использовать генератор списков.
list_of_str = ['drgrd', 'gdg']
new_list = [f'{list_of_str.index(string)} - {string}' for string in list_of_str]
print(new_list)