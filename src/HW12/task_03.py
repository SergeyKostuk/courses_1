# Создать класс Point, описывающий точку(атрибуты x, y).
# Создать класс Figure. Создать три дочерних класса Circle(атрибуты: координаты центра(тип Point), длина радиуса; методы: нахождение периметра и площади окружности),
# Triangle(атрибуты: три точки, методы: нахождение площади и периметра), Square(атрибуты: две точки, методы: нахождение площади и периметра).
# При потребности создавать все необходимые методы не описанные в задании
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self):
        return (self.x, self.y)


class Figure:
    def vector_length(self, X, Y):
        return ((Y.x - X.x) ** 2 + (Y.y - X.y) ** 2) ** 0.5


class Circle(Figure):
    def __init__(self, point, radius):
        self.radius = radius
        self.point = point
    def square(self):
        return 3.14 * self.radius ** 2

    def perimetr(self):
        return 3.14 * self.radius * 2


class Triangle(Figure):
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def perimetr(self):
        AB = self.vector_length(self.A, self.B)
        AC = self.vector_length(self.A, self.C)
        BC = self.vector_length(self.B, self.C)
        return AB + BC + AC

    def square(self):
        return abs(0.5 * ((self.A.x - self.C.x) * (self.B.y - self.C.y)) - (
                (self.A.y - self.C.y) * (self.B.x - self.C.x)))


class Square(Figure):
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def perimetr(self):
        D = super().vector_length(self.A, self.B)
        return 4 * D / 2 ** 0.5

    def square(self):
        D = super().vector_length(self.A, self.B)
        return D * D / 2


def main():
    circle = Circle(Point(3, 4), 5)
    print(circle.perimetr())
    A = Point(3, -3)
    B = Point(7, -3)
    C = Point(5, 5)
    tr = Triangle(A, B, C)
    sq = Square(A, B)
    print(tr.perimetr())
    print(sq.square())


if __name__ == "__main__":
    main()
