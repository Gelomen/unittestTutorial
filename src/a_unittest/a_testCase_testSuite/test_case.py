# encoding=utf-8
# 测试用例

import unittest


# 被测试类

class MyClass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        return a - b


# 测试类

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """初始化类固件"""
        print("---- setUpClass\n")

    @classmethod
    def tearDownClass(cls):
        """重构类固件"""
        print("---- tearDownClass\n")

    # 初始化工作
    def setUp(self):
        self.a = 3
        self.b = 1
        print("-- setUp")

    # 退出清理工作
    def tearDown(self):
        print("-- tearDown")

    # 具体的测试用例，一定要以 test 开头
    def test_sum(self):
        # 断言两数之和是否为 4
        self.assertEqual(MyClass.sum(self.a, self.b), 4, 'test sum fail')

    def test_sub(self):
        # 断言两数只差是否为 2
        self.assertEqual(MyClass.sub(self.a, self.b), 2, 'test sub fail')


# 启动单元测试
if __name__ == '__main__':
    unittest.main()
