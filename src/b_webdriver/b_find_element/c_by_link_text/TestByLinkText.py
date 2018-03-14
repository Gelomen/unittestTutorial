# encoding=utf-8

import unittest
from selenium import webdriver


class TestByLinkText(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///E:/Gelomen/PycharmProjects/unittestTutorial/src/b_webdriver/b_find_element/test.html")

    def tearDown(self):
        self.driver.quit()

    def test_find_element_by_link_text(self):
        self.driver.find_element_by_link_text("百度搜索")
        self.driver.find_element_by_link_text("搜狗搜索")


if __name__ == "__main__":
    unittest.main()
