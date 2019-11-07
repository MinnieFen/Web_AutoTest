# coding:utf-8
from time import sleep
from PageObject.LoginPageObject import Login
from ruamel import yaml
from Base.DriverBase import start_driver
from config import readconfig
import os
class get_cookie():
    def __init__(self):
        self.driver = start_driver()
        self.login = Login(self.driver)
# 封装元素操作方法
    def save_cookie(self,phone,psw,url):
        self.login.psw_login(phone,psw,url)
        login_cookie = self.driver.get_cookie(name = 'laravel_session')
        yamlpath = os.path.abspath(os.path.dirname(__file__)) + '\login_cookie.yaml'
        cookie_value = login_cookie
        with open(yamlpath,'w',encoding='utf-8') as f:
            yaml.dump(cookie_value,f,Dumper=yaml.RoundTripDumper)
        # self.d.delete_cookie(name = 'laravel_session')
        # self.d.refresh()
        self.driver.quit()
# if __name__ == '__main__':
#     cookie = get_cookie()
#     phone = readconfig.inputPhone_cookie
#     psw = readconfig.inputPsw_cookie
#     url = readconfig.url_login
#     cookie.save_cookie(phone,psw,url)