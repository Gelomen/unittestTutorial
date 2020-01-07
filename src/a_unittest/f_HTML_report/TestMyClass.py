# encoding=utf-8

import unittest
import math


class Calc(object):

    @staticmethod
    def add(x, y, *d):
        # 加法计算
        result = x + y
        for i in d:
            result += i
        return result

    @staticmethod
    def sub(x, y, *d):
        # 减法计算
        result = x - y
        for i in d:
            result -= i
        return result


class SuiteTestCalc(unittest.TestCase):
    def setUp(self):
        self.c = Calc()

    def tearDown(self):
        pass

    def test_sub(self):
        self.assertEqual(self.c.sub(100, 34, 6), 61, "求差结果错误！")

    def test_add(self):
        self.assertEqual(self.c.add(1, 32, 56), 90, "求和结果错误！")


class SuiteTestPow(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        pass

    def test_pow(self):
        self.assertEqual(pow(6, 3), 216, "求幂结果错误！")

    def test_hasattr(self):
        self.assertTrue(hasattr(math, "pow"), "检测的属性不存在！")
