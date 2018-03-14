# encoding=utf-8

import unittest
from src.a_unittest.d_discover.Calc import Calc


class MyTest(unittest.TestCase):
    c = None

    @classmethod
    def setUpClass(cls):
        cls.c = Calc()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_add(self):
        self.assertEqual(MyTest.c.add(1, 2, 12), 15, "test add fail")
