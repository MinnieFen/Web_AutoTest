# coding:utf-8
from selenium import webdriver
from time import sleep
from case.login import Login
# d = webdriver.Firefox()
# d.maximize_window()
# inputPhone = '18782038146'
# inputPassword = 'a123456'
# companyName = '汇众金控集团1'
# # 登录操作
# url = 'http://qiyuebao-t.yunxitech.cn/'
# d.get(url)
# d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
# d.find_element_by_id('login_span_type_pwd').click()
# d.find_element_by_id('login_id_input_phone').send_keys(inputPhone)
# d.find_element_by_id('login_id_input_password').send_keys(inputPassword)
# d.find_element_by_class_name('ui-checkbox').click()
# d.find_element_by_id('login_id_login').click()
# sleep(3)
#
# d.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
# d.find_element_by_link_text('我的账户').click()
# sleep(3)
# d.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div/ul/li[2]/a/span').click()
# d.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div/ul/li[2]/ul/li[1]/a/i').click()
# d.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[1]/div[2]/input').send_keys(companyName)
# d.find_element_by_id('dialog_add_company_submit').click()
# now_company = d.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div/ul/li[2]/a/span').text
# if now_company  == companyName:
#     print('add company success!')
# else:
#     print('add company fail!')
#

class addCom():
    def __init__(self):
        self.dv = webdriver.Firefox()
    def add_com(self,companyName):
        Login().login(inputPhone,inputPassword)
        self.dv.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
        self.dv.find_element_by_link_text('我的账户').click()
        sleep(3)
        self.dv.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div/ul/li[2]/a/span').click()
        self.dv.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div/ul/li[2]/ul/li[1]/a/i').click()
        self.dv.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[1]/div[2]/input').send_keys(companyName)
        self.dv.find_element_by_id('dialog_add_company_submit').click()
        now_company = self.dv.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div/ul/li[2]/a/span').text
        if now_company == companyName:
            print('add company success!')
        else:
            print('add company fail!')
if __name__ == '__main__':
    companyName = '金控集团2'
    inputPhone = '18782038146'
    inputPassword = 'a123456'
    addCom().add_com(companyName)