a = [
     {'number': 401, 'year': 1999},
     {'number': 402, 'year': 1990},
     {'number': 403, 'year': 2000},
     {'number': 407, 'year': 199},
     ]
n = int(input('year?\n'))
b = [i for i in a if i['year'] > n]
print(b)
