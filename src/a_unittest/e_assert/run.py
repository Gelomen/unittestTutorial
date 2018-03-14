# encoding=utf-8

import unittest
import HTMLTestReportCN

if __name__ == "__main__":
    test_suite = unittest.TestLoader().discover(".")

    filename = ".\\test_report.html"
    fp = open(filename, "wb")
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title="Find elements report", description="通过id、name、link text、tag name、class name、xpath、css selector查找元素", tester="Gelomen")
    runner.run(test_suite)
    fp.close()

    print("\033[36;0m--------------------- 测试结束 ---------------------\033[0m")
