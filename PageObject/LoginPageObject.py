# coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from config import readconfig
from Base import get_exceldata
from Base.operate_page import BasePage
from Base.SQLconnect import MySQLUtil
from PageElements.LoginPageElements import login_elements
class Login(object):
    def __init__(self):
        self.d = webdriver.Firefox()
        url = readconfig.url_login
        self.d.get(url)
        self.B = BasePage(self.d)
        self.B.max_window()
        self.getdata = get_exceldata.get_excel_data('loginpage')
        self.data0 = self.getdata[0]['elements']    # 跳转到登录页面元素
        self.data1 = self.getdata[1]['elements']    # 切换密码登录元素
        self.data2 = self.getdata[2]['elements']    # 输入手机号
        self.data3 = self.getdata[3]['elements']    # 输入密码/验证码
        self.data4 = self.getdata[4]['elements']    # 确定登录/确定重置密码
        self.data5 = self.getdata[5]['elements']    # 登录成功header显示的用户名
        self.data6 = self.getdata[6]['elements']    # 点击获取验证码
        self.data7 = self.getdata[7]['elements']    # 点击忘记密码
        self.data8 = self.getdata[8]['elements']    # 输入新密码
        self.data9 = self.getdata[9]['elements']    # 跳转到注册页面
        self.data10 = self.getdata[10]['elements']  # 输入注册手机号
        self.data11 = self.getdata[11]['elements']  # 输入注册密码
        self.data12 = self.getdata[12]['elements']  # 输入注册用户名
        self.data13 = self.getdata[13]['elements']  # 点击注册获取验证码
        self.data14 = self.getdata[14]['elements']  # 输入注册验证码
        self.data15 = self.getdata[15]['elements']  # 勾选同意服务协议框
        self.data16 = self.getdata[16]['elements']  # 确定注册按钮
        self.data17 = self.getdata[17]['elements']  # 返回首页
        self.data18 = self.getdata[18]['elements']  # 点击退出按钮
        self.new_psw = get_exceldata.get_excel_data('new_pswData')  # 读取新密码
        self.register_data = get_exceldata.get_excel_data('register')   # 读取注册账号信息
# 密码登录
    def psw_login(self):
        inputPhone = readconfig.inputPhone_login
        inputPsw = readconfig.inputPsw_login
        a = login_elements()[0]
        self.B.click_btn(By.XPATH,a)
        # self.B.click_btn(By.XPATH,self.data0)
        self.B.click_btn(By.XPATH, self.data1)
        self.B.send_word(inputPhone, By.XPATH, self.data2)
        self.B.send_word(inputPsw, By.XPATH, self.data3)
        self.B.click_btn(By.XPATH, self.data4)
        sleep(5)
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
if __name__ == '__main__':
    Login().psw_login()