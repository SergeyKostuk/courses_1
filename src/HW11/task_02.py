# Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5), стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные.
class Car:
    def __init__(self, model, year, speed=0):
        self.__model = model
        self.__year = year
        self.__speed = speed

    c = 12
    def rasing(self):
        self.__speed += 5


    def slowdown(self):
        self.__speed -= 5


    def stop(self):
        self.__speed = 0


    def speed_view(self):
        print(self.__speed)


    def reverse(self):
        self.__speed *= -1


def main():
    car = Car('tesla', 2018)
    car.rasing()
    car.reverse()
    car.slowdown()
    car.stop()
    car.rasing()
    car.__speed


if __name__ == '__main__':
    main()
