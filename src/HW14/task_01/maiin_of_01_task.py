from file_fith_classess import (
    Animal,
    WildAnimal,
    Pet,
    Lion,
    Wolf,
    Cat,
    Dog,
)


def main():
    lion = Lion()
    lion.scratch()
    cat = Cat()
    cat.scratch()
    dog = Dog()
    dog.swim()
    wolf = Wolf()
    wolf.swim()


if __name__ == "__main__":
    main()
