# encoding=utf-8
# 按顺序执行测试用例

import unittest
from src.a_unittest.b_sequence.Calc import Calc


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(u"单元测试前，创建 Calc 类的实例")
        cls.c = Calc()

    @classmethod
    def tearDownClass(cls):
        pass

    # 具体的测试用例，一定要以 test 开头
    def test_add(self):
        self.assertEqual(self.c.add(1, 2, 12), 15, "test add fail")

    def test_sub(self):
        self.assertEqual(self.c.sub(2, 1, 3), -2, "test sub fail")

    def test_mul(self):
        self.assertEqual(Calc.mul(2, 3, 5), 30, "test mul fail")

    def test_div(self):
        self.assertEqual(Calc.div(8, 2, 4), 1, "test div fail")


if __name__ == "__main__":
    # a_unittest.main() 这个执行方法，是将所有用例按照 ASCII码 顺序执行

    # 获取TestSuite的实例对象
    suite = unittest.TestSuite()

    # 将测试用例添加到容器里，执行的顺序将按照这个添加顺序执行
    suite.addTest(MyTest("test_mul"))
    suite.addTest(MyTest("test_div"))
    suite.addTest(MyTest("test_add"))
    suite.addTest(MyTest("test_sub"))

    # 创建 TextTestRunner 实例对象
    unittest.TextTestRunner(verbosity=2).run(suite)
