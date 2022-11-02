import unittest
import math

class Calc:
    def __init__(self) -> None:
        pass

    def add(self, x1, x2):
        return (x1 , x2)

    def multiply(self, x1, x2):
        return x1 * x2

    def subtract(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x2 == 0:
            return 'no no'
        return x1 / x2




class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 5), 10)
        self.assertEqual(self.calc.add(0.0001, 0.0002), 0.0003)
        self.assertEqual(self.calc.add(4, 7), 11)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(0.25, 0.25), 0.0625)
        self.assertEqual(self.calc.multiply(5, 1), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(0.001, 0.0001), 0.0009)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 5), 1)
        self.assertEqual(self.calc.divide(100, 0.01), 10000)
        self.assertEqual(self.calc.divide(100, 0), 'no no')


unittest.main()