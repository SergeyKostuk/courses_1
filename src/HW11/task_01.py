class Vilage:

    def __init__(self, name, size, population):
        self.__name = name
        self.__size = size
        self.__population = population

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        self.__population = population

    def info(self):
        print(f'{1000-self.__population} residents more to become a town')

    def grow(self):
        self.__population += 100


class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def is_adult(self):
        if self.__age >= 18:
            return True
        return False

    def Bd(self):
        self.__age += 1


class University:
    def __init__(self, name, proffesors, students):
        self.__name = name
        self.__proffesors = proffesors
        self.__students = students

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def proffesors(self):
        return self.__proffesors

    @proffesors.setter
    def proffesors(self, proffesors):
        self.__proffesors = proffesors

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students):
        self.__students = students

    def one_left(self):
        a = self.__proffesors.pop()
        return a

    def bad_session(self):
        self.__students -= 100

    def new_year(self):
        self.__students += 700


class President:
    def __init__(self, surname='L', time=20, debt=99999999):
        self.__surname = surname
        self.__time = time
        self.__debt = debt

    @property
    def surname(self):
        return f'{self.__surname} and we see him again'

    @surname.setter
    def surname(self, surname):
        if surname != 'L':
            print('no way!!')
        else:
            self.__surname = surname

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time

    @property
    def debt(self):
        return self.__debt

    @debt.setter
    def time(self, debt):
        self.__debt = debt

    def departure(self):
        return 'sorry but movment stop for an hour '


def main():
    vilage = Vilage('my_vil', 80, 150)
    vilage.size = 3000
    print(vilage.size)
    vilage.grow()
    print(vilage.population)
    vilage.info()
    person = Person('vova', 'strah', 19)
    print(person.is_adult())
    person.age = 17
    person.Bd
    print(person.is_adult())
    univ = University('BSUIR', ['Smirnova', 'Smirnov', 'Makovskii'], 1000)
    print(univ.one_left())


if __name__ == '__main__':
    main()
