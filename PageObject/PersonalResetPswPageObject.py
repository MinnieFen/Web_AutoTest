# coding:utf-8
from Base.BasePage import BasePage
from time import sleep
from Base.GetLoginCookie import Cookie
from selenium import webdriver
from config import readconfig
from selenium.webdriver.common.by import By
from public.SQLconnect import MySQLUtil
from public.GetExcelData import get_excel_data


mysql = MySQLUtil(db=readconfig.sql_db_qiyuebao)
sqldata = get_excel_data('sql_data')

reset_psw_list = (By.XPATH,'/html/body/div[1]/div[1]/div/nav/ul/li[7]/a/span')  # 侧边栏修改密码
code_text = (By.XPATH,'//*[@id="verification-code"]')  # 验证码输入框
get_code = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/div[2]/div[1]/div/span/button')   # 获取验证码按钮
new_psw = (By.XPATH,'//*[@id="new-pwd"]')    # 新密码输入框
reset_btn = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/p/button')   # 确定修改密码按钮
code_toast = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/p/span')  # 前端页面提示 请输入验证码
psw_toast = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/p/span')   # 前端页面提示 请输入新密码
reset_success_text = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a')

class Reset_psw(BasePage):
    # 保持登录状态
    # def keep_login_cookie(self,url):
    #     return Cookie(self.driver).keep_login(url)
    # 点击侧边栏修改密码
    def click_reset_list(self):
        # self.keep_login_cookie(url)
        # sleep(3)
        self.click_btn(*reset_psw_list)
        sleep(3)
    # 点击验证码按钮
    def click_code(self):
        self.click_reset_list()
        self.click_btn(*get_code)
        sleep(5)

    # 连接数据库，获取验证码
    def get_code(self,search,table,where):
        return mysql.select(search,table,where)

    # 输入验证码
    def send_code(self,code):
        self.clear_word(*code_text)
        self.send_word(code,*code_text)
        sleep(2)
     # 输入新密码
    def send_new_psw(self,newpsw):
        self.clear_word(*new_psw)
        self.send_word(newpsw,*new_psw)
        sleep(3)
    # 确定修改按钮
    def reset_button(self):
        self.click_btn(*reset_btn)
        sleep(3)
    # 未输入验证码弹框提示
    def code_toast(self):
        return self.get_text(*code_toast)
    # 未输入密码弹框提示
    def psw_toast(self):
        return self.get_text(*psw_toast)
    # 都为空点击确认
    def reset_psw_empty(self):
        self.click_reset_list()
        self.reset_button()
        sleep(3)
    # 确定修改密码
    def reset_psw(self,code,newpsw):
        self.send_code(code)
        self.send_new_psw(newpsw)
        self.reset_button()
    # def handle(self):
    #     self.get_handle()

    # 重置密码成功后，退出页面，获取页面【首页】文字
    def get_reset_text(self):
        return self.get_text(*reset_success_text)