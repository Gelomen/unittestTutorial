# encoding=utf-8

import unittest
from functools import reduce


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.num = 5

    def test_factorial(self):
        seq = range(1, self.num + 1)

        res = reduce(lambda x, y: x * y, seq)

        self.assertEqual(res, 120, "factorial fail")
