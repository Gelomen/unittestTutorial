# encoding=utf-8

import unittest
from src.lib.Browser import Browser
from src.b_webdriver.b_find_element.Common import Common


class TestByLinkText(unittest.TestCase):

    def setUp(self):
        self.browser = Browser().browser(location="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.get()

    def tearDown(self):
        self.browser.quit()

    def test_find_element_by_link_text(self):
        self.browser.find_element_by_link_text("百度搜索")
        self.browser.find_element_by_link_text("搜狗搜索")


if __name__ == "__main__":
    unittest.main()
