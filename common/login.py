# coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from config import readconfig
from common.operate_page import BasePage
from common import get_exceldata
from ruamel import yaml
import os
class Login(object):
    def __init__(self):
        self.d = webdriver.Chrome()
        url = readconfig.url
        self.d.get(url)
        self.B = BasePage(self.d)
        self.B.max_window()
        getdata = get_exceldata.get_excel_data('loginpage')
        self.data1 = getdata[0]['elements']
        self.data2 = getdata[1]['elements']
        self.data3 = getdata[2]['elements']
        self.data4 = getdata[3]['elements']
        self.data5 = getdata[4]['elements']
        self.data6 = getdata[5]['elements']
# 封装元素操作方法
    def test_login(self):
        inputPhone = readconfig.inputPhone
        inputPsw = readconfig.inputPsw
        # B = BasePage(self.d)
        ele1 = (By.XPATH,self.data1)
        ele2 = (By.XPATH,self.data2)
        ele3 = (By.XPATH,self.data3)
        ele4 = (By.XPATH,self.data4)
        ele5 = (By.XPATH,self.data5)
        self.B.click_btn(*ele1)
        self.B.click_btn(*ele2)
        self.B.send_word(inputPhone,*ele3)
        self.B.send_word(inputPsw,*ele4)
        self.B.click_btn(*ele5)
        sleep(3)
        login_cookie = self.d.get_cookie(name = 'laravel_session')
        yamlpath = os.path.abspath(os.path.join(os.getcwd())) + '\login_cookie.yaml'
        cookie_value = login_cookie
        with open(yamlpath,'w',encoding='utf-8') as f:
            yaml.dump(cookie_value,f,Dumper=yaml.RoundTripDumper)
        self.d.delete_cookie(name='laravel_session')
        self.d.quit()

if __name__ == '__main__':
    Login().test_login()