# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число
res = 0
N = int(input())
for i in range(1, N + 1):
    res += 1 / i
print(f' s is {res}')