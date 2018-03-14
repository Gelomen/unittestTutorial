# encoding=utf-8
# 测试结果生成HTML文件

import unittest
import math
import HTMLTestReportCN  # 目前官网的HTMLTestRunner只支持python2.7，所以使用别人优化的CN版，https://github.com/findyou/HTMLTestRunnerCN


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

    def test_sub(self):
        self.assertEqual(self.c.sub(100, 34, 6), 61, "求差结果错误！")

    def test_add(self):
        self.assertEqual(self.c.add(1, 32, 56), 90, "求和结果错误！")


class SuiteTestPow(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_pow(self):
        self.assertEqual(pow(6, 3), 216, "求幂结果错误！")

    def test_hasattr(self):
        self.assertTrue(hasattr(math, "pow"), "检测的属性不存在！")


if __name__ == "__main__":

    suite1 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestCalc)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestPow)
    suite = unittest.TestSuite([suite1, suite2])
    # a_unittest.TextTestRunner().run(suite)

    # 定义报告文件的路径，目录要先创建好
    filename = ".\\report\\test_report.html"

    # 以二进制方式打开文件，准备写
    fp = open(filename, "wb")

    # 使用 HTMLTestRunner 配置参数，输出报告路径、标题、描述、测试人员
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title="测试报告", description="测试报告详细描述", tester="Gelomen")

    # 运行测试集合
    runner.run(suite)

    # 文件操作关闭，记得加这句，否则报告没有内容
    fp.close()
