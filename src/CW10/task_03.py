from functools import reduce

result = reduce(lambda a, x: a * x, filter(lambda x: not x % 3, [1, 2, 3, 4, 5, 6]), 1)
print(result)
result = reduce(lambda a, x: a * x, ([x for x in [1, 2, 3, 4, 5, 6] if not x % 3]), 1)
print(result)
