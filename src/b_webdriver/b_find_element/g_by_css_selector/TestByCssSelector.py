# encoding=utf-8

import unittest
from src.lib.Browser import Browser
from src.b_webdriver.b_find_element.Common import Common


class TestByCssSelector(unittest.TestCase):

    def setUp(self):
        self.browser = Browser().browser(location="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.get()

    def tearDown(self):
        self.browser.quit()

    def test_find_element_by_css_selector(self):
        # 用最对定位，查找第一个div中的 “查询” 按钮
        self.browser.find_element_by_css_selector("html > body > div > input[value='查询']")

        # 用相对定位，查找第一个div中的 “查询” 按钮
        self.browser.find_element_by_css_selector("input[value='查询']")

        # 通过class定位
        self.browser.find_element_by_css_selector("a.orange")

        # 通过ID定位
        self.browser.find_element_by_css_selector("input#div1input")

        # 使用页面其他元素定位
        self.browser.find_element_by_css_selector("img[alt='div1-img1']")
        self.browser.find_element_by_css_selector("img[alt='div1-img1'][href='https://www.sogou.com']")

        # 使用属性的部分内容定位，符号与等号之间不能有空格，如 “href ^ = ”是错误的
        self.browser.find_element_by_css_selector("a[href ^='https://www.so']")  # 以 https://www.so 开头的href属性
        self.browser.find_element_by_css_selector("a[href $='gou.com']")  # 以 gou.com 结尾的href属性
        self.browser.find_element_by_css_selector("a[href *='so']")  # 包含 so 的href属性

        # 查找子元素
        self.browser.find_element_by_css_selector("div#div1 > input#div1input")
        # 查找后代元素，一般不止1个所以是 elements
        self.browser.find_elements_by_css_selector("div input")

        # 伪类定位，前三个定位的冒号前一定要有空格，否则无法正确定位
        self.browser.find_element_by_css_selector("div#div1 :first-child")  # 找到第一个子元素
        self.browser.find_element_by_css_selector("div#div1 :nth-child(2)")  # 找到第二个子元素，若要找第三个则 nth-child(3)
        self.browser.find_element_by_css_selector("div#div1 :last-child")  # 找到最后一个子元素
        self.browser.find_element_by_css_selector("input:focus")  # 找到当前获取焦点的input元素
        self.browser.find_elements_by_css_selector("input:enabled")  # 找到当前可操作的input元素
        self.browser.find_elements_by_css_selector("input:checked")  # 找到当前已勾选的input元素
        self.browser.find_element_by_css_selector("input:not([id])")  # 找到当前没有 id 属性的input元素

        # 查找同级兄弟元素
        # 查找id为div1的 div 元素下跟 input 元素同级且临近 input 元素的元素 a
        self.browser.find_element_by_css_selector("div#div1 > input + a")
        # 查找id为div1的 div 元素下跟 input 和 a 元素同级且临近 a 元素的元素 img
        self.browser.find_element_by_css_selector("div#div1 > input + a + img")
        # 查找id为div1的 div 元素下跟 input 和 任意类型的元素同级且临近这个任意类型元素的元素 img，* 只能代表一个任意类型元素
        self.browser.find_element_by_css_selector("div#div1 > input + * + img")
        # 查找id为 recordlist 的 ul 元素下，查找 p 元素后的所有 li 元素
        self.browser.find_elements_by_css_selector("ul#recordlist > p ~ li")

        # 同时获取多个元素，id为div1的div、所有input 和 所有a
        self.browser.find_elements_by_css_selector("div#div1,input,a")


if __name__ == "__main__":
    unittest.main()
