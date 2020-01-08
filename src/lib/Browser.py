# coding=utf-8

from selenium import webdriver


class Browser(object):

    # webdriver 初始化
    @staticmethod
    def browser(headless=False, location="./chromedriver.exe"):
        if headless:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=location)
        else:
            browser = webdriver.Chrome(executable_path=location)

        return browser
