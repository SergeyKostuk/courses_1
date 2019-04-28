from abc import ABC, abstractmethod
from interfaces import (
    FelineInterface,
    CanineInterface,
)


class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass


class Pet(Animal):
    pass


class WildAnimal(Animal):
    pass


class Cat(Pet, FelineInterface):

    def voice(self):
        print('meow')

    def scratch(self):
        print('cats have claws ')


class Dog(Pet, CanineInterface):
    def swim(self):
        print('dogs like swimming')

    def voice(self):
        print('Woof,woof')


class Lion(WildAnimal, FelineInterface):
    def scratch(self):
        print('lions have big claws ')

    def voice(self):
        print('RRRRR-rrrr')


class Wolf(WildAnimal, CanineInterface):
    def voice(self):
        print('auuuuuuuuuuuuuuuuuu')

    def swim(self):
        print('wolves can swim ')
