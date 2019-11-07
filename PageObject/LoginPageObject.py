# coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from config import readconfig
from Base import GetExcelData
from Base.BasePage import BasePage
from Base.SQLconnect import MySQLUtil
from PageElements.LoginPageElements import login_elements
from Base.DriverBase import start_driver
class Login(BasePage):
    # def __init__(self):
    #     self.d = start_driver()
    #     # url = readconfig.url_login
    #     # self.d.get(url)
    #     self.B = BasePage(self.d)
    # 打开页面
    # def open_page(self):
    #     self.url = readconfig.url_login
    #     self.open_url(self.url)
    # 跳转到登录页面
    def login_page(self):
        self.click_btn(*(login_elements()[0]))
    # 切换密码登录
    def psw_login_page(self):
        self.click_btn(*(login_elements()[1]))
    # 登录手机号
    def login_phone(self,inputPhone):
        self.clear_word(*(login_elements()[2]))
        self.send_word(inputPhone,*(login_elements()[2]))
    # 登录密码
    def login_psw(self,inputPsw):
        self.clear_word(*(login_elements()[3]))
        self.send_word(inputPsw,*(login_elements()[3]))
    # 确定登录按钮
    def login_button(self):
        self.click_btn(*(login_elements()[4]))
    # 密码登录
    def psw_login(self,inputPhone,inputPsw,url):
        self.open_url(url)
        self.login_page()
        self.psw_login_page()
        self.login_phone(inputPhone)
        self.login_psw(inputPsw)
        self.login_button()
        sleep(2)
    # 登录成功用户名
    def login_success_username(self):
        return self.get_text(*(login_elements()[5]))
    # 前端错误信息提示
    def login_error_page(self):
        return self.get_text(*(login_elements()[19]))
    # 服务器错误信息提示
    def login_error_sever(self):
        return self.get_text(*(login_elements()[20]))

# 验证码登录
    def code_login(self):
        inputPhone = readconfig.inputPhone_cookie
        self.B.click_btn(By.XPATH,self.data0)
        self.B.send_word(inputPhone,By.XPATH,self.data2)
        self.B.click_btn(By.XPATH,self.data6)
        sleep(5)
        mysql = MySQLUtil()
        sql = '''SELECT `CODE` from sms_code_record WHERE PHONE = '18782038146' ORDER BY CTIME DESC'''
        mysql.get_execute(sql)
        codes = mysql.get_rows(sql)
        mysql.mysql_close()
        self.B.send_word(codes[0],By.XPATH,self.data3)
        sleep(3)
        self.B.click_btn(By.XPATH,self.data4)
# 退出登录
    def logout(self):
        self.B.click_btn(By.XPATH,self.data17)
        sleep(2)
        self.B.click_btn(By.XPATH,self.data5)
        self.B.click_btn(By.XPATH,self.data18)
# 忘记密码
    def psw_reset(self):
        inputPhone = readconfig.inputPhone_cookie
        self.B.click_btn(By.XPATH,self.data0)
        self.B.click_btn(By.XPATH,self.data7)
        self.B.clear_word(By.XPATH,self.data2)
        self.B.send_word(inputPhone,By.XPATH,self.data2)
        self.B.click_btn(By.XPATH,self.data6)
        sleep(5)
        mysql = MySQLUtil()
        sql = '''SELECT `CODE` from sms_code_record WHERE PHONE = '18782038146' ORDER BY CTIME DESC'''
        mysql.get_execute(sql)
        codes = mysql.get_rows(sql)
        mysql.mysql_close()
        self.B.send_word(codes[0],By.XPATH,self.data3)
        self.B.send_word(self.new_psw,By.XPATH,self.data8)
        self.B.click_btn(By.XPATH,self.data4)
# 注册账号
    def register(self):
        self.B.click_btn(By.XPATH,self.data9)
        self.B.send_word(self.register_data['phone'],By.XPATH,self.data10)
        self.B.send_word(self.register_data['psw'],By.XPATH,self.data11)
        self.B.send_word(self.register_data['name'],By.XPATH,self.data12)
        self.B.click_btn(By.XPATH,self.data13)
        sleep(5)
        mysql = MySQLUtil()
        sql = '''SELECT `CODE` from sms_code_record WHERE PHONE = '18782038146' ORDER BY CTIME DESC'''
        mysql.get_execute(sql)
        codes = mysql.get_rows(sql)
        mysql.mysql_close()
        self.B.send_word(codes[0],By.XPATH,self.data14)
        self.B.click_btn(By.XPATH,self.data15)
        self.B.click_btn(By.XPATH,self.data16)
# if __name__ == '__main__':
#     login = Login(driver=webdriver.Firefox())
#     login.psw_login('18782038145','a123456','http://qiyuebao-t.yunxitech.cn/')
