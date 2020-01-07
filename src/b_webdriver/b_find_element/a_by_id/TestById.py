# encoding=utf-8

import unittest
from src.lib.Browser import Browser
from src.lib.HTMLTestReportCN import ReportDirectory
from src.b_webdriver.b_find_element.Common import Common


class TestById(unittest.TestCase):

    def setUp(self):
        self.browser = Browser().browser(location="../../lib/chromedriver.exe")
        self.report_dir = ReportDirectory()
        self.common = Common(self.browser)
        self.common.get()

    def tearDown(self):
        self.browser.quit()

    def test_find_element_by_id(self):
        try:
            self.browser.find_element_by_id("username")
            self.browser.find_element_by_id("passwords")
        except Exception:
            self.report_dir.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    unittest.main()
