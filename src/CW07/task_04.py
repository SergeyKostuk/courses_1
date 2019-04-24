def my_func(**kwargs):
    for key, value in kwargs.items():
        if not len(key) % 2:
            print(key, value)


my_dict = {'ab': 3, 'c': 4, '31513534': 40101010}
my_func(**my_dict)
