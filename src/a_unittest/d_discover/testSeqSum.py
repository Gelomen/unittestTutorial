# encoding=utf-8

import unittest


class MyTestCase(unittest.TestCase):

    def test_equal(self):
        seq = range(11)
        self.assertEqual(sum(seq), 55, "sum fail")
