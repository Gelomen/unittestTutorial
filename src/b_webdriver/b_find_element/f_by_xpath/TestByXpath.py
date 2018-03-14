# encoding=utf-8

import unittest
from selenium import webdriver


class TestByXpath(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///E:/Gelomen/PycharmProjects/unittestTutorial/src/b_webdriver/b_find_element/test.html")

    def tearDown(self):
        self.driver.quit()

    def test_find_element_by_xpath(self):
        """ ----------------------- """

        """ 1. 使用绝对路径，以单斜杠“/”开头，但脆弱 """
        self.driver.find_element_by_xpath("/html/body/div/input[@value='查询']")

        """ 2. 使用相对路径，以双斜杠“//”开头 """
        self.driver.find_element_by_xpath("//input[@value='查询']")

        """ 3. 使用索引号 """
        # 若改为input[3]会报错，因为起始位置为每个div，而被测试HTML文件里，每个div下最多只有2个input标签
        self.driver.find_element_by_xpath("//input[2]")
        # 定位最后一个div元素的a标签
        self.driver.find_element_by_xpath("//div[last()]/a")
        # 定位倒数第二个div元素的a标签
        self.driver.find_element_by_xpath("//div[last()-1]/a")
        # 获取当前元素 input 的位置序列号，且条件为小于2
        self.driver.find_element_by_xpath("//div/input[position()<2]")

        """ 4. 使用页面元素定位 """
        # 定位被测试页中第一张 img 元素
        self.driver.find_element_by_xpath("//img[@alt='div1-img1']")
        # 定位页面第一张图片
        self.driver.find_element_by_xpath("//img[@href='https://www.sogou.com']")
        # 定位页面第二个div中第一个input输入框
        self.driver.find_element_by_xpath("//div[@id='div2']/input[@name='div2input']")
        # 定位第一个div中第一个链接
        self.driver.find_element_by_xpath("//div[@id='div1']/a[@href='https://www.sogou.com']")
        # 定位页面的查询按钮
        self.driver.find_element_by_xpath("//input[@type='button']")

        """ 5. 使用模糊属性值定位，适合在很多场景使用 """
        # 定位 alt 属性的属性值以“div1”关键字开头的元素
        self.driver.find_element_by_xpath("//img[starts-with(@alt,'div1')]")
        # 定位 alt 属性的属性值包含“img”关键字的元素，包含即可，无须考虑位置
        self.driver.find_element_by_xpath("//img[contains(@alt,'img1')]")

        """ 6. 轴定位，先找到一个相对好定位的元素，再以它为轴，根据它和要定位元素间的相对位置关系进行定位，可解决一些元素难定位的问题 """
        # --- parent 选取当前节点的父节点
        self.driver.find_element_by_xpath("//img[@alt='div2-img2']/parent::div")
        # --- child 选取当前节点的所有子节点
        self.driver.find_element_by_xpath("//div[@id='div1']/child::img")
        # --- ancestor 选取当前节点的所有先辈节点
        self.driver.find_element_by_xpath("//img[@alt='div2-img2']/ancestor::div")
        # --- descendant 选取当前节点的所有后代节点
        self.driver.find_element_by_xpath("//div[@id='div2']/descendant::img")
        # --- following 选取当前节点的开始标签之后的所有节点
        self.driver.find_element_by_xpath("//div[@id='div1']/following::img")
        # --- following-sibling 选取当前节点之后的所有同级节点
        self.driver.find_element_by_xpath("//a[@href='https://www.baidu.com']/following-sibling::input")
        # --- preceding 选取当前节点的开始标签之前的所有节点
        self.driver.find_element_by_xpath("//img[@alt='div2-img2']/preceding::div")
        # --- preceding-sibling 选取当前节点之前的所有同级节点
        self.driver.find_element_by_xpath("//input[@value='查询']/preceding-sibling::a[1]")
        # 轴后加 * ，表示通配符，找到 value 为 “查询”的input元素前面的所有同级元素，但不包括input本身
        self.driver.find_element_by_xpath("//input[@value='查询']/preceding-sibling::*")

        """ 7. 使用表达式 """
        # （1）使用 text() 函数定位文本
        self.driver.find_element_by_xpath("//a[text()='搜狗搜索']")
        # （2） “.” 与 text() 等价
        self.driver.find_element_by_xpath("//a[.='搜狗搜索']")
        # （3） 使用模糊匹配方法，搭配文本定位
        self.driver.find_element_by_xpath("//a[contains(.,'百度')]")
        # （4） 与（3）等价
        self.driver.find_element_by_xpath("//a[contains(text(),'百度')]")
        # （5）选择上层父元素 div
        self.driver.find_element_by_xpath("//a[contains(text(),'百度')]/preceding::div")
        # （6）“..” 与 preceding::div 等价
        self.driver.find_element_by_xpath("//a[contains(text(),'百度')]/..")

        """ 运算符 """
        # 获取两个或多个集合
        self.driver.find_elements_by_xpath("//div | //a | //input")
        # 索引号相加
        self.driver.find_element_by_xpath("//div[1+1]")
        # 索引号相减
        self.driver.find_element_by_xpath("//div[2-1]")
        # 索引号相乘
        self.driver.find_element_by_xpath("//div[1*2]")
        # 索引号相除，因为通常的除号“/”是特殊符号，所以XPath的除号是 div
        self.driver.find_element_by_xpath("//div[4 div 2]")
        """ 文本判断必须用 . 或者 text() """
        # 判断文本，等于
        self.driver.find_element_by_xpath("//div[text() =5]//span[. =2]")
        # 或者如下，即：用自己做判断的，需要用 text()= ，参照7（1），如果是用子节点做判断的，直接a[b=c]
        self.driver.find_element_by_xpath("//div[span =2]/span[. =2]")
        # 判断文本，不等于
        self.driver.find_element_by_xpath("//div[a !=10]")
        # 判断文本，小于
        self.driver.find_element_by_xpath("//span[text() <14]//div[a <11]")
        # 判断文本，小于等于
        self.driver.find_element_by_xpath("//span[text() <=13]//div[a <=8]")
        # 判断文本，大于
        self.driver.find_element_by_xpath("//a[text() >2]")
        # 判断文本，大于等于
        self.driver.find_element_by_xpath("//span[text() >=12]//div[a >=7]")
        # 判断文本,and
        self.driver.find_element_by_xpath("//span[text() >1 and text() <=5]")
        self.driver.find_element_by_xpath("//div[a <9 and span =12]")
        # 判断文本，or
        self.driver.find_element_by_xpath("//span[text() =10 or text() =13]")
        self.driver.find_element_by_xpath("//div[a<=8 or span=13]")
        # 判断文本，mod 取余
        self.driver.find_element_by_xpath("//div[7 mod 3]")  # 7 mod 3 = 1
        self.driver.find_element_by_xpath("//span[11 mod 3]")  # 11 mod 3 = 2


if __name__ == "__main__":
    unittest.main()
