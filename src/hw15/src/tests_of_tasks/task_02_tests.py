import unittest
from hw15.src.tasks.task_02 import Point, Triangle, Circle, Square, Figure


class PointTests(unittest.TestCase):
    def setUp(self):
        self.point_1 = Point(1, 1)
        self.point_2 = Point(3, 3)

    def test_point_x(self):
        result = self.point_2.x
        self.assertEqual(result, 3)


class FigureTests(unittest.TestCase):
    def setUp(self):
        self.point_1 = Point(1, 1)
        self.point_2 = Point(3, 3)
        self.dist = Figure()

    def test_calc_dist(self):
        result = self.dist.calc_dist(self.point_1, self.point_2)
        self.assertEqual(result, 8 ** 0.5)


class CircleTests(unittest.TestCase):
    def setUp(self):
        self.point_1 = Point(1, 1)

        self.circle = Circle(self.point_1, 3)

    def test_calc_area(self):
        result = round(self.circle.calc_area(), 3)
        self.assertEqual(result, 28.274)

    def test_calc_perimeter(self):
        result = round(self.circle.calc_perimeter(), 3)
        self.assertEqual(result, 18.85)


class TriangleTests(unittest.TestCase):
    def setUp(self):
        self.point_1 = Point(0, 1)
        self.point_2 = Point(3, 3)
        self.point_3 = Point(4, 4)
        self.triangle = Triangle(self.point_1, self.point_2, self.point_3)

    def test_calc_area(self):
        result = round(self.triangle.calc_area(), 3)
        self.assertEqual(result, 0.5)

    def test_calc_perimeter(self):
        result = round(self.triangle.calc_perimeter(), 3)
        self.assertEqual(result, 10.02)


class SquareTests(unittest.TestCase):
    def setUp(self):
        self.point_1 = Point(0, 2)
        self.point_2 = Point(2, 0)
        self.square = Square(self.point_1, self.point_2)

    def test_calc_area(self):
        result = round(self.square.calc_area())
        self.assertEqual(result, 4)

    def test_calc_perimeter(self):
        result = round(self.square.calc_perimeter())
        self.assertEqual(result, 8)
