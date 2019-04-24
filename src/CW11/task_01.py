class Dog:

    def __init__(self, name, height, weight, age, master, adress='Minsk'):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__master = master
        self.__adress = adress

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, adress):
        self.__adress = adress


def main():
    dog = Dog('bob', 80, 15, 7, 'Sergey')
    dog.master = 'Moe'
    print(dog.master)


if __name__ == '__main__':
    main()
