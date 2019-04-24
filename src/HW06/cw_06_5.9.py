# Написать игру. Пользователь должен угадать число. Сперва вводиться диапазон угадывания.
# После колличество попыток. В случае правильного ответа - выводить You are the winner.
# В случае неправильного давать игроку подсказку(больше или меньше искомое число).
# Если за указанное количество попыток число не угадано - выводить:
# You are the loser и правильное число.
from random import randint

begin_of_gap, end_of_gap = int(input('from ')), int(input('to '))
num_of_tries = int(input('num of tries: '))
if begin_of_gap < end_of_gap:
    X_number = randint(begin_of_gap, end_of_gap)
else:
    print('wrong input')
i = 0
while i < num_of_tries:
    i += 1
    guess = int(input('your guess: '))
    if guess == X_number:
        print('You are the winner')
        break
    elif i == num_of_tries:
        continue
    elif guess < X_number:
        print('go higher')
    elif guess > X_number:
        print('lower')
else:
    print(f'You are the loser the right number is {X_number}')
