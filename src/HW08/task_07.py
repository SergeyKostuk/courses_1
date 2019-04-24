# Описать функцию fact2( n ) вещественного типа, вычисляющую двойной факториал :n!! = 1·3·5·...·n,
# если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа.
# С помощью этой функции найти двойные факториалы пяти данных целых чисел [01-11.2-Proc35]
#
#


def fuct2(n):
    if type(n) != int or n < 0:
        c = "n is only int and n > 0"
        return c
    else:
        res = 1
        if not n % 2:
            for i in range(1, n + 1):
                if not i % 2:
                    res *= i
        elif n % 2:
            for i in range(1, n + 1):
                if i % 2:
                    res *= i

    return res


c = [6, 7, 12, -5, 0]
for i in c:
    print(f'{i}!! = {fuct2(i)}')
