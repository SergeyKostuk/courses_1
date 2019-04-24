class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('ruuuun')

    def jump(self):
        print('is jumping')

    def birthday(self):
        self.age += 1


class Dog(Pet):

    def bark(self):
        print('Woof,woof')


class Cat(Pet):

    def meow(self):
        print('meow')


class Parot(Pet):

    def fly(self):
        print('flyyy')


a = Cat('Lev', 5, 'Alex')
a.meow()
a.jump()
print(a.name)
