# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
# т. е. таким, которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)[03-10.32]


def find_palindrome(word):
    if type(word) == str and len(word.split()) == 1:

        word = word.lower()
        if word == word[::-1]:
            return f'{word} is polindrom'
        return f'{word} is`t polindrom'

    return 'wrong input'


print(find_palindrome('blalb'))
