# Для каждого натурального числа в промежутке от m до n вывести все делители, кроме единицы и самого числа. m и n вводятся с клавиатуры.
import time
start_time = time.time()
m = int(input('m = '))
n = int(input('n = '))

if m > 0 and m < n:
    for i in range(m, n + 1):
        a = []
        for num in range(2, i // 2 + 1):
            if not i % num:
                a.append(str(num))
        print(f'{i}: {" ".join(a)}')

else:
    print("wrong input")
print('---- %sseconds ---' % (time.time()-start_time))