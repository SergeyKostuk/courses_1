# Создать класс Book. Атрибуты: количество страниц, год издания, автор, цена. Добавить валидацию в конструкторе на ввод корректных данных. Создать иерархию ошибок.
class OnlyIntException(Exception):
    def __init__(self, message='only int please sir '):
        super().__init__(message)


class OnlyPositiveException(Exception):
    def __init__(self, message='only positive numbers please sir '):
        super().__init__(message)


class OnlyStrException(Exception):
    def __init__(self, message='only string please sir '):
        super().__init__(message)


class OnlyFloatException(Exception):
    def __init__(self, message='only float please sir '):
        super().__init__(message)


class Book:
    def __init__(self, pages, year, author, cost):
        if type(pages) != int:
            raise OnlyIntException()
        elif pages < 0:
            raise OnlyPositiveException()

        self.pages = pages

        if type(year) != int:
            raise OnlyIntException()
        elif year < 0:
            raise OnlyPositiveException()
        self.year = year
        if not isinstance(author, str):
            raise OnlyStrException()
        self.author = author
        if not isinstance(cost, float):
            raise OnlyFloatException()
        self.cost = cost


def main():
    try:
        b = Book(5, 6, -5, '3.55')
    except OnlyIntException as err:
        print(f'{err}')
    except OnlyPositiveException as err:
        print(f'{err}')
    except OnlyStrException as err:
        print(f'{err}')
    except OnlyFloatException as err:
        print(f'{err}')




