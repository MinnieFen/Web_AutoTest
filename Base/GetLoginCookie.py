# coding:utf-8
from time import sleep
from PageObject.LoginPageObject import Login
from ruamel import yaml
from Base.DriverBase import DriverBase
from config import readconfig
from Base.BasePage import BasePage
import os
import ruamel
import warnings
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)
class Cookie():
    def __init__(self):
        self.driverBase = DriverBase()
        self.driver = self.driverBase.open_broswer()
        self.login = Login(self.driver)
# 封装元素操作方法
    def save_cookie(self,phone,psw,url):
        self.login.psw_login(phone,psw,url)
        login_cookie = self.driver.get_cookie(name = 'laravel_session')
        yamlpath = os.path.abspath(os.path.dirname(__file__)) + '\login_cookie.yaml'
        cookie_value = login_cookie
        with open(yamlpath,'w',encoding='utf-8') as f:
            yaml.dump(cookie_value,f,Dumper=yaml.RoundTripDumper)
        sleep(3)
        self.driverBase.quit_broswer()
        # self.driver.delete_cookie(name = 'laravel_session')
        # self.driver.refresh()
    def get_cookie(self,phone,psw,url,yamlName="login_cookie.yaml"):
        self.save_cookie(phone,psw,url)
        f = os.path.abspath(os.path.dirname(__file__))
        p = f + '\login_cookie.yaml'
        f = open(p)
        value = f.read()
        cookie_all = yaml.load(value)
        cookie_name = cookie_all['name']
        cookie_value = cookie_all['value']
        cookie_data_dict = {'name': cookie_name, 'value': cookie_value}
        # print(cookie_data_dict)
        return cookie_data_dict
    def keep_login(self,phone,psw,urlcookie,url):
        cookieData = self.get_cookie(phone,psw,urlcookie)
        base = BasePage(self.driver)
        base.open_url(url)
        self.driver.add_cookie(cookieData)
        base.open_url(url)
        self.driver.implicitly_wait(10)
# if __name__ == '__main__':
#     cookie = Cookie()
#     phone = readconfig.inputPhone_cookie
#     psw = readconfig.inputPsw_cookie
#     urlcookie = readconfig.url_login
#     url = readconfig.url_admin
#     cookie.keep_login(phone,psw,urlcookie,url)