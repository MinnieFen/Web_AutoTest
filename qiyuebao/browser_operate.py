# coding:utf-8
from selenium import webdriver
class Browser():
    def open_browser(self,browser):
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        return self.driver
    def max_browser(self):
        pass
if __name__ == '__main__':
    browser = 'firfox'
    Browser = Browser()
    Browser.open_browser(browser)