# encoding=utf-8

import unittest
from selenium import webdriver


class TestById(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///E:/Gelomen/PycharmProjects/unittestTutorial/src/b_webdriver/b_find_element/test.html")

    def tearDown(self):
        self.driver.quit()

    def test_find_element_by_id(self):
        self.driver.find_element_by_id("username")
        self.driver.find_element_by_id("password")


if __name__ == "__main__":
    unittest.main()
