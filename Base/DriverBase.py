# coding:utf-8
from selenium import webdriver
from config import readconfig

def start_driver():
    driverName = readconfig.browserName
    if driverName == 'Firefox' or driverName == 'firefox':
        driver = webdriver.Firefox()
    elif driverName == 'Chrome' or driverName == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Ie()
    return driver
