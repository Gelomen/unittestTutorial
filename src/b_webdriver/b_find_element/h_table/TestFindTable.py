# encoding=utf-8

import unittest
from src.lib.Browser import Browser
from src.b_webdriver.b_find_element.Common import Common


class TestFindTable(unittest.TestCase):

    def setUp(self):
        self.browser = Browser().browser(location="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.get()

    def tearDown(self):
        self.browser.quit()

    def test_find_element_by_css_selector(self):
        # 获取整个table对象
        table = self.browser.find_element_by_id("table")
        # 获取所有行
        tr_list = table.find_elements_by_tag_name("tr")
        # 先断言获取的行数是否正确
        assert len(tr_list) == 5, "表格行数错误！"

        for row in tr_list:
            # td_list =
            row.find_elements_by_tag_name("td")
            # for col in td_list:
            #     print(col.text, end="\t")
            # print()

        # 获取表格第二行第二列单元格，获取表格内容必须先通过 tbody
        self.browser.find_element_by_xpath("//*[@id='table']/tbody/tr[2]/td[2]")
        self.browser.find_element_by_css_selector("table#table > tbody > tr:nth-child(2) > td:nth-child(2)")

        # 获取表格的子元素 input 的value值
        cream = self.browser.find_element_by_xpath("//td[contains(., '化妆')]/input[1]").get_attribute("value")
        self.assertEqual(cream, "面霜", "找不到面霜文本！")


if __name__ == "__main__":
    unittest.main()
