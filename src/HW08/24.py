from math import factorial
def sine(x):
    sum = 0.0
    n = 0.0
    term = 1.0
    while (term > .0000000001):
        #loops until the iterations grow so large that 'term' becomes negligibly small
        term = ((x ** (2 * n + 1.0))) / (factorial(2 * n + 1.0))
        if n % 2 == 0:
            sum += term
        else:
            sum -= term
        n += 1
    return sum
print(sine(42))