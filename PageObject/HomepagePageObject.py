# coding:utf-8
from Base.BasePage import BasePage
from time import sleep
from Base.GetLoginCookie import Cookie
from selenium import webdriver
from config import readconfig
from selenium.webdriver.common.by import By
from public.SQLconnect import MySQLUtil
from public.GetExcelData import get_excel_data

homepage_lsit = (By.XPATH,'/html/body/div[1]/div[1]/div/nav/ul/li[1]/a/span')
contract_total = (By.XPATH,'//*[@id="admin_span_my_credit_all_count"]')
contract_wait_confirm = (By.XPATH,'//*[@id="admin_span_my_confirm_credit_count"]')
contract_wait_appraise = (By.XPATH,'//*[@id="admin_span_my_appraisal_credit_count"]')
contract_wait_complete = (By.XPATH,'//*[@id="admin_span_my_done_credit_count"]')

VIP = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div[3]/p[4]/a[1]')
class HomePage(BasePage):
    # 保持登录状态
    def keep_login_cookie(self,url):
        return Cookie(self.driver).keep_login(url)
    # 点击侧边栏首页
    def click_homepage_list(self,url):
        self.keep_login_cookie(url)
        sleep(3)
        self.click_btn(*homepage_lsit)
        sleep(5)
    # 获取我的履约总数
    def my_contract(self):
        return self.get_text(*contract_total)
    # 获取待我确认的履约数量
    def wait_confirm(self):
        return self.get_text(*contract_wait_confirm)
    # 获取待我评价的履约数量
    def wait_appraise(self):
        return self.get_text(*contract_wait_appraise)
    # 获取待我完成的履约数量
    def wait_complete(self):
        return self.get_text(*contract_wait_complete)