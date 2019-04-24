# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]
import datetime

m = int(input('m = '))
n = int(input('n = '))
a = []
b = []
print(datetime.datetime.now())
if m > 0 and m < n:
    for i in range(m, n + 1):
        amount_of_dividers = 0
        second_amount_of_dividers = 0
        for num in range(1, i // 2 + 1):
            if not i % num:
                amount_of_dividers += num
        if amount_of_dividers in range(m, n + 1):
            for j in range(1, amount_of_dividers // 2 + 1):
                if not amount_of_dividers % j:
                    second_amount_of_dividers += j
        if second_amount_of_dividers == i and amount_of_dividers != second_amount_of_dividers and i not in b:
            a.append(i)
            b.append(amount_of_dividers)
couples = list(zip(a, b))
for couple in couples:
    print(couple)
print(datetime.datetime.now())
