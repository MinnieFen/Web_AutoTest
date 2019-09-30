# coding:utf-8
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('Selenium')
driver.find_element_by_id('su').click()

driver.quit()
