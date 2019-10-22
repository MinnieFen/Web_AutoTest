# coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('http://qiyuebao-t.yunxitech.cn/?lg=0')
driver.find_element_by_link_text('登录').click()
driver.find_element_by_id('login_span_type_pwd').click()
driver.find_element_by_id('login_id_input_phone').send_keys('18782038146')
driver.find_element_by_id('login_id_input_password').send_keys('a123456')
driver.find_element_by_id('login_id_login').click()
sleep(3)
driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
driver.find_element_by_link_text('我的账户').click()
