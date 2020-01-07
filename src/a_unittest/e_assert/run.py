# encoding=utf-8

import unittest
from src.lib import HTMLTestReportCN

if __name__ == "__main__":
    title = "Find elements report"
    des = "通过id、name、link text、tag name、class name、xpath、css selector查找元素"
    tester = "Gelomen"
    test_suite = unittest.TestLoader().discover(".")

    filename = ".\\test_report.html"
    fp = open(filename, "wb")
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=title, description=des, tester=tester)
    runner.run(test_suite)
    fp.close()
