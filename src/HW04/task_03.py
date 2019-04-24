# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’})
dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
i = 0
#dict1_keys = list(dict1.keys())
dict1_keys = list(dict1)
keys_len = len(dict1_keys)     #лучше вынести переменную так как в вайле будет каждый раз пересчитывать
while i < keys_len:
    old_key = dict1_keys[i]
    new_key = f'{dict1_keys[i]}{len(dict1_keys[i])}'
    dict1[new_key] = dict1.pop(old_key)
    i += 1
print(dict1)
print(type(dict1.keys()))
