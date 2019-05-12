import unittest
from hw15.src.tasks.task_01 import MyTime


class MyTimeTests(unittest.TestCase):
    def setUp(self):
        self.time_1 = MyTime(1, 12, 59)
        self.time_2 = MyTime('1-12-60')
        self.time_3 = MyTime()
        self.time_4 = MyTime(MyTime('1-12-60'))

    def test_time_to_sec_int(self):
        result = self.time_1.time_to_seconds()
        self.assertEqual(result, 4379)

    def test_time_to_sec_str(self):
        result = self.time_2.time_to_seconds()
        self.assertEqual(result, 4380)

    def test_time_to_sec_none(self):
        result = self.time_3.time_to_seconds()
        self.assertEqual(result, 0)

    def test_time_to_sec_my_time(self):
        result = self.time_4.time_to_seconds()
        self.assertEqual(result, 4380)

    def test_seconds_to_time(self):
        result = self.time_3.seconds_to_time(4379)
        self.assertEqual(result, (1, 12, 59))

    def test_eq(self):
        result = self.time_4 == self.time_2
        self.assertTrue(result)

    def test_ne(self):
        result = self.time_1 != self.time_2
        self.assertTrue(result)

    def test_lt(self):
        result = self.time_1 < self.time_2
        self.assertTrue(result)

    def test_gt(self):
        result = self.time_2 > self.time_1
        self.assertTrue(result)

    def test_le(self):
        result = self.time_1 <= self.time_2
        self.assertTrue(result)

    def test_ge(self):
        result = self.time_2 >= self.time_2
        self.assertTrue(result)

    def test_add(self):
        result = self.time_1 + self.time_2
        self.assertEqual(result, MyTime(2, 25, 59))

    def test_sub(self):
        result = self.time_2 - self.time_1
        self.assertEqual(result, MyTime(0, 0, 1))

    def test_sub_negative_res(self):
        result = self.time_1 - self.time_2
        self.assertEqual(result, MyTime(0, 0, 0))

    def test_mul(self):
        result = self.time_1 * 2
        self.assertEqual(result, MyTime(2, 25, 58))

    def test_str(self):
        result = str(self.time_1)
        self.assertEqual(result, f'{self.time_1.hours}-{self.time_1.minutes}-{self.time_1.seconds}')
