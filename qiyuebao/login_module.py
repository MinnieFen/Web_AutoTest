# coding:utf-8
from selenium import webdriver
import os
from time import sleep
import unittest
from selenium.webdriver.common.by import By

def openBrowser():
    '''return webdriver handle'''
    webdriver_handle = webdriver.Firefox()
    return webdriver_handle
def openUrl(handle,url):
    '''load url'''
    handle.get(url)
    # d.maximize_window()
def findElement(d,**arg):

def login(inputPhone,inputPassword):
    d = openBrowser()
    openUrl(d,url)
    d.maximize_window()
    # url = 'http://qiyuebao-t.yunxitech.cn/'
    # d.get(url)
    d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
    d.find_element_by_id('login_span_type_pwd').click()
    d.find_element_by_id('login_id_input_phone').send_keys(inputPhone)
    d.find_element_by_id('login_id_input_password').send_keys(inputPassword)
    d.find_element_by_class_name('ui-checkbox').click()
    d.find_element_by_id('login_id_login').click()
    sleep(3)
    userName = d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').text
    if userName == u'晨曦':
        print('登录成功')
    else:
        print('user name error!')
        # self.d.quit()
    # def logout(self):
    #     self.d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
    #     self.d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/ul/li[4]/a').click()
    # def quit(self):
    #     self.d.quit()

if __name__ == '__main__':
    inputPhone = '18782038146'
    inputPassword = 'a123456'
    login(inputPhone,inputPassword)
    # Login().logout()
#     Login().quit()