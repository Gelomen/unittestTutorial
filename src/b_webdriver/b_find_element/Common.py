# encoding=utf-8


class Common(object):

    def __init__(self, browser):
        self.browser = browser
        self.url = "file:///G:/work/X/unittestTutorial/src/b_webdriver/b_find_element/test.html"

    def get(self):
        self.browser.get(self.url)