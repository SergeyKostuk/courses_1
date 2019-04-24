number_1 = int(input())
summ = 0
multipl = 1
while number_1 > 0:
    if number_1 % 10 !=0:
        multipl *= number_1 % 10
    summ += number_1 % 10
    number_1 = number_1 // 10
print(multipl)
print(summ)
