# coding:utf-8
from selenium import webdriver
import os
from time import sleep
import unittest
from selenium.webdriver.common.by import By

# d = webdriver.Firefox()
# d.get('http://qiyuebao-t.yunxitech.cn/')
# d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
# d.find_element_by_id('login_span_type_pwd').click()
# d.find_element_by_id('login_id_input_phone').send_keys('18782038146')
# d.find_element_by_id('login_id_input_password').send_keys('a123456')
# d.find_element_by_class_name('ui-checkbox').click()
# d.find_element_by_id('login_id_login').click()

# def login():
#     d = webdriver.Firefox()
#     d.maximize_window()
#     inputPhone = '18782038146'
#     inputPassword = 'a123456'
#     url = 'http://qiyuebao-t.yunxitech.cn/'
#     d.get(url)
#     d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
#     d.find_element_by_id('login_span_type_pwd').click()
#     d.find_element_by_id('login_id_input_phone').send_keys(inputPhone)
#     d.find_element_by_id('login_id_input_password').send_keys(inputPassword)
#     d.find_element_by_class_name('ui-checkbox').click()
#     d.find_element_by_id('login_id_login').click()
#     sleep(3)
#     userName = d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').text
#     if userName == u'晨曦':
#         print('登录成功')
#     else:
#         print('user name error!')
#     # 退出
#     d.find_element_by_class_name('dropdown-toggle').click()
#     sleep(2)
#     d.find_element_by_link_text('退出').click()
# if __name__ == '__main__':
#     login()

class Login():
    def __init__(self):
        self.d = webdriver.Firefox()
        self.d.maximize_window()
        # url = 'http://qiyuebao-t.yunxitech.cn/'
        # self.d.get(url)
        self.d.implicitly_wait(30)
        # self.d.quit()
    def login(self,inputPhone,inputPassword):
        url = 'http://qiyuebao-t.yunxitech.cn/'
        self.d.get(url)
        self.d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
        self.d.find_element_by_id('login_span_type_pwd').click()
        self.d.find_element_by_id('login_id_input_phone').send_keys(inputPhone)
        self.d.find_element_by_id('login_id_input_password').send_keys(inputPassword)
        self.d.find_element_by_class_name('ui-checkbox').click()
        self.d.find_element_by_id('login_id_login').click()
        sleep(3)
        userName = self.d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').text
        if userName == u'晨曦':
            print('登录成功')
        else:
            print('user name error!')
        # self.d.quit()
    def logout(self):
        self.d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
        self.d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/ul/li[4]/a').click()
    def quit(self):
        self.d.quit()

if __name__ == '__main__':
    inputPhone = '18782038146'
    inputPassword = 'a123456'
    Login().login(inputPhone,inputPassword)
    Login().logout()
#     Login().quit()