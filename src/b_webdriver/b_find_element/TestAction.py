# encoding=utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class TestAction(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///E:/Gelomen/PycharmProjects/unittestTutorial/src/b_webdriver/b_find_element/test.html")

    def tearDown(self):
        self.driver.quit()

    def test_find_element_by_css_selector(self):
        sleep(5)
        baidu_img = self.driver.find_element_by_xpath("//img[@alt='div2-img2']")
        ActionChains(self.driver).move_to_element_with_offset(baidu_img, 370, 272).click().perform()
        sleep(5)


if __name__ == "__main__":
    unittest.main()
