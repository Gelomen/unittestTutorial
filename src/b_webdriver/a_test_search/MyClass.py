# encoding=utf-8

import unittest
from selenium import webdriver
import time


class MyClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.get("http://sogou.com")

        self.driver.find_element_by_id("query").clear()

        self.driver.find_element_by_id("query").send_keys(u"Webdriver 实战宝典")

        self.driver.find_element_by_id("stb").click()

        time.sleep(3)

        assert u"吴晓华" in self.driver.page_source, "页面中不存在要寻找的关键字"


if __name__ == "__main__":
    # unittest.main()

    test_case = unittest.TestLoader().loadTestsFromTestCase(MyClass)
    suite = unittest.TestSuite(test_case)

    runner = unittest.TextTestRunner(verbosity=2).run(suite)
