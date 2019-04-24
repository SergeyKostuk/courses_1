def factorial(n):
    z = 1
    for i in range(1, n+1):
        z *= i
    return z


print(factorial(5))
print(factorial(10))
print(factorial(0))

