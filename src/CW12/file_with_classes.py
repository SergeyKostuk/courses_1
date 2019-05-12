import random
from abc import ABC, abstractmethod

class Pet(ABC):
    counter = 0
    __private_counter = 0

    def __init__(self, name, age, master, height, weight):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

        self.is_alive = True

        Pet.counter += 1
        Pet.__private_counter += 1

    @classmethod
    def get_counter(cls):
        return cls.__private_counter
    #TASK-01 HW13
    @staticmethod
    def random_name():
        letter = chr(random.randrange(97, 97 + 26)).upper()
        return f'{letter}-{random.randint(1, 99)}'

    def run(self):
        print('ruuuun')

    def jump(self):
        print('is jumping')

    def birthday(self):
        self.age += 1

    def change_weight(self, weight=None):
        self.weight += weight if weight else 0.2

    def change_height(self, height=None):
        self.height += height if height else 0.2
    @abstractmethod
    def voice(self):
        pass


class Dog(Pet):

    def voice(self):
        print('Woof,woof')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 13:
                self.is_alive = False


class Cat(Pet):

    def voice(self):
        print('meow')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 16:
                self.is_alive = False


class Parrot(Pet):
    def __init__(self, name, age, master, height, weight, species):
        super().__init__(name, age, master, height, weight)
        self.species = species

    def fly(self):

        if self.weight > 0.1:
            print('This par cant fly')
        else:
            print('flyyy')

    def change_height(self, height=None):

        self.height += height if height else 0.05

    def change_weight(self, weight=None):
        self.weight += weight if weight else 0.05

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 60:
                self.is_alive = False

    def voice(self):
        print('meow')
class Horse(Pet):

    def voice(self):
        print('IGO-go')


class Donkey(Pet):

    def voice(self):
        print('IA-ia IA-ia')


class Mule(Donkey, Horse):
    pass
