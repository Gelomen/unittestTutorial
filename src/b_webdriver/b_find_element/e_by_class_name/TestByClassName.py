# encoding=utf-8

import unittest
from selenium import webdriver


class TestByClassName(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///E:/Gelomen/PycharmProjects/unittestTutorial/src/b_webdriver/b_find_element/test.html")

    def tearDown(self):
        self.driver.quit()

    def test_find_element_by_class_name(self):
        self.driver.find_element_by_class_name("orange")
        self.driver.find_element_by_class_name("cadet")


if __name__ == "__main__":
    unittest.main()
