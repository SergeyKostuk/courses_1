#Создать lambda функцию, которая принимает на вход неопределенное количество именных аргументов и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}
print((lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(a=5, b=7))
# my_dict = {'a' : 3, 'b' : 4}
# print((lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(**my_dict))
