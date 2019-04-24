# Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы сравнения, сложения, вычитания, умножения на число, вывод на экран.
# Перегрузить конструктор на обработку входных параметров вида: одна строка, три числа, другой объект класса MyTime, и отсутствие входных параметров.
# Примечание: http://sheregeda.github.io/blog/2015/01/18/maghichieskiie-mietody-python/
from datetime import datetime


class MyTime:
    def __init__(self, hours=None, minutes=None, seconds=None):
        if type(hours) == str:
            one_date = list(map(int, hours.split(':')))

            self.hours = one_date[0]
            self.minutes = one_date[1]
            self.seconds = one_date[2]
        elif hours and minutes and seconds:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        elif hours == None:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0


        else:
            self.hours = hours.hours
            self.minutes = hours.minutes
            self.seconds = hours.seconds

    def __gt__(self, other):
        if self.hours > other.hours:
            return self.hours > other.hours
        elif self.hours == other.hours:
            if self.minutes > other.minutes:
                return self.minutes > other.minutes

            elif self.minutes == other.minutes:
                if self.seconds > other.seconds:
                    return self.seconds > other.seconds
                elif self.seconds == other.seconds:
                    return False

    def __lt__(self, other):
        return other > self

    def __eq__(self, other):
        if not self > other and not self < other:
            return True
        else:
            return False

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True

    def __add__(self, otherObj):
        self.hours += otherObj.hours
        self.minutes += otherObj.minutes
        self.seconds += otherObj.seconds
        return MyTime(self)

    def __sub__(self, otherObj):
        self.hours -= otherObj.hours
        self.minutes -= otherObj.minutes
        self.seconds -= otherObj.seconds
        return MyTime(self)

    def __mul__(self, num):
        self.hours *= num
        self.minutes *= num
        self.seconds *= num
        return MyTime(self)


def main():
    a = MyTime('12:52:13')
    b = MyTime('12:52:13')

    print(a != b)

    print(str(b.minutes))


if __name__ == "__main__":
    main()
