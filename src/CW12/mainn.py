from file_with_classes import (
    Pet,
    Parrot,
    Cat,
    Dog,
    Mule,
    # Horse,
    Donkey,
)


def func(animals):
    for animal in animals:
        animal.voice()


def main():

    cat = W('Lev', 5, 'Alex', 3, 4)
    # print(Pet.get_counter())

    # dog = Dog('Kesha', 3, 'Sergey', 12, 10)
    # func([cat, dog, parrot])
    # print(parrot.is_alive)
    # parrot.birthday()
    # parrot.birthday()
    # print(parrot.species)
    # print(parrot.is_alive)
    # parrot.fly()
    # parrot.change_weight()
    # parrot.change_weight()
    # parrot.fly()
    # parrot.change_weight(1)
    # print(parrot.weight)
    # print(Pet.counter)
    # print(Pet.get_counter())
    # print(cat.get_counter())
    # mule = Mule('Kesha', 59, 'Sergey', 12, 0)
    # print(Pet.random_name())

if __name__ == '__main__':
    main()
