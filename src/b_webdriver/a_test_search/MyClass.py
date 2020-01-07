# encoding=utf-8

import unittest
import time
from src.lib.Browser import Browser


class MyClass(unittest.TestCase):

    def setUp(self):
        self.browser = Browser().browser(headless=False, location="../../lib/chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def test_search(self):
        self.browser.get("http://www.baidu.com")

        self.browser.find_element_by_id("kw").clear()

        self.browser.find_element_by_id("kw").send_keys(u"Webdriver")

        self.browser.find_element_by_id("su").click()

        time.sleep(3)

        assert u"Webdriver" in self.browser.page_source, "页面中不存在要寻找的关键字"


if __name__ == "__main__":
    # unittest.main()

    test_case = unittest.TestLoader().loadTestsFromTestCase(MyClass)
    suite = unittest.TestSuite(test_case)

    runner = unittest.TextTestRunner(verbosity=2).run(suite)
