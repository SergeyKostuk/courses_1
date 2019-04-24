from task_01_clases import (
    Parrot,
    Cat,
    Dog,
)


def func(list_of_aminals):
    for animal in list_of_aminals:
        animal.voice()


def main():
    parrot = Parrot('Kesha', 59, 'Sergey', 12, 0, 'wave')
    cat = Cat('Lev', 5, 'Alex', 3, 4)
    dog = Dog('Kesha', 3, 'Sergey', 12, 10)
    func([cat, dog, parrot])


if __name__ == '__main__':
    main()
