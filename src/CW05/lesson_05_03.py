n = int(input())
m = int(input())
res = 0
for i in range(n, m):
    res += i ** 3
print(res)

# from random import randint
# res = 0
# for i in range(randint(0, 5), randint(5, 9)):
#      res += i ** 3
# print(res)
