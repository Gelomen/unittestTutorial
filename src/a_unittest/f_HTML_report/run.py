# encoding=utf-8
# 测试结果生成HTML文件

import unittest
from src.lib import HTMLTestReportCN

if __name__ == "__main__":
    suite = unittest.TestLoader().discover(".")
    # a_unittest.TextTestRunner().run(suite)

    # 定义报告文件的路径，目录要先创建好
    filename = ".\\reports\\test_report.html"
    # 以二进制方式打开文件，准备写
    fp = open(filename, "wb")
    # 使用 HTMLTestRunner 配置参数，输出报告路径、标题、描述、测试人员
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title="测试报告", description="测试报告详细描述", tester="Gelomen")
    # 运行测试集合
    runner.run(suite)
    # 文件操作关闭，记得加这句，否则报告没有内容
    fp.close()
