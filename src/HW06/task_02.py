#Дано число. Найти сумму и произведение его цифh
number = int(input("enter a number:\n"))
the_sum = 0
the_multiplication = 1
number = str(number)
for i in number:
    the_sum += int(i)
    the_multiplication *= int(i)
print(f'sum: {the_sum}')
print(f'multiplication: {the_multiplication}')
