# coding:utf-8
from selenium import webdriver
from config import readconfig
# def start_driver():
#     driverName = readconfig.browserName
#     if driverName == 'Firefox' or driverName == 'firefox':
#         driver = webdriver.Firefox()
#     elif driverName == 'Chrome' or driverName == 'chrome':
#         driver = webdriver.Chrome()
#     else:
#         driver = webdriver.Ie()
#     return driver
class DriverBase():
    def __init__(self):
        self.driverName = readconfig.browserName
        if self.driverName == 'Firefox' or self.driverName == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.driverName == 'Chrome' or self.driverName == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Ie()
    def open_broswer(self):
        driver = self.driver
        return driver
    def quit_broswer(self):
        return self.driver.quit()
    def max_window(self):
        return self.driver.maximize_window()