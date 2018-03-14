# encoding=utf-8
# 测试套件


import unittest
import random


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        pass

    def test_choice(self):
        # 从序列 seq 中随机选取一个元素
        element = random.choice(self.seq)
        # 验证随机元素是否属于序列中
        self.assertTrue(element in self.seq)

    def test_sample(self):
        # 验证执行的语句是否抛出异常
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def tearDown(self):
        pass

    def test_shuffle(self):
        # 随机打乱原 seq 的顺序
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        # 验证执行函数时抛出了 TypeError 异常
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


if __name__ == '__main__':
    # unittest.main()
    # 根据给定的测试类，获取其中的所有以 "test" 开头的测试方法，并返回一个测试套件
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testCase2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFunctions)
    # 将多个测试类加载到测试套件中
    suite = unittest.TestSuite([testCase1, testCase2])
    # 设置 verbosity = 2， 可以打印更详细的执行信息
    unittest.TextTestRunner(verbosity=2).run(suite)
