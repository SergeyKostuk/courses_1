#8) В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы. [02-7.2-HL08]
string_1 = input('your string -->:\n')
string_1 = string_1.split(' ')
string_1 = ' '.join(string_1[::-1])
print(f'new string:\n{string_1}')
