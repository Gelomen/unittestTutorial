# encoding=utf-8

import unittest
import os
import sys
curPath = os.path.abspath("../")
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])
from src.lib import HTMLTestReportCN

if __name__ == "__main__":
    report_dir = HTMLTestReportCN.ReportDirectory(path="./report/")
    report_dir.create_dir()
    report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")

    title = "Find elements report"
    dec = "通过id、name、link text、tag name、class name、xpath、css selector查找元素"
    tester = "Gelomen"
    test_suite = unittest.TestLoader().discover(".")

    # filename = ".\\report\\test_report.html"
    fp = open(report_path, "wb")
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=title, description=dec, tester=tester)
    runner.run(test_suite)
    fp.close()
