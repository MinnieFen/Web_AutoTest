# coding:utf-8
from Base.BasePage import BasePage
from time import sleep
from PageElements.AddContractPageElement import addContract_elements
from Base.GetLoginCookie import Cookie
from selenium import webdriver
from config import readconfig

class Add_Contract(BasePage):
    # 点击侧边栏我的契约,，点击添加契约按钮
    def contract_list(self):
        self.click_btn(*(addContract_elements()[0]))
        # self.click_btn(*(addContract_elements()[1]))
    # 点击添加契约按钮
    def add_contract_button(self):
        self.click_btn(*(addContract_elements()[1]))
    # 输入公司名称，搜索
    def company_name(self,companyName):
        self.send_word(companyName,*(addContract_elements()[2]))
        self.click_btn(*(addContract_elements()[3]))
    # 选择第一个公司
    def select_company(self):
        self.click_btn(*(addContract_elements()[4]))
    # 选择契约月份
    def select_time(self):
        self.click_btn(*(addContract_elements()[5]))
        self.click_btn(*(addContract_elements()[6]))
    # 输入契约描述
    def contract_describe(self,contract_word):
        self.send_word(contract_word,*(addContract_elements()[7]))
    # 选择已完成契约
    def select_finish_contracr(self,contract_appraise):
        self.click_btn(*(addContract_elements()[8]))
        self.send_word(contract_appraise,*(addContract_elements()[9]))
        self.click_btn(*(addContract_elements()[10]))
        self.click_btn(*(addContract_elements()[11]))
        self.click_btn(*(addContract_elements()[12]))
        self.click_btn(*(addContract_elements()[13]))
        self.click_btn(*(addContract_elements()[14]))
    # 选择未完成契约
    def select_unfinish_contract(self):
        self.click_btn(*(addContract_elements()[15]))
    # 选择我方使用防伪印章
    def select_use_stamp(self):
        self.click_btn(*(addContract_elements()[16]))
    # 选择对方使用防伪印章
    def select_other_use_stamp(self):
        self.click_btn(*(addContract_elements()[17]))
    # 确认添加契约
    def add_contracr_verify(self):
        self.click_btn(*(addContract_elements()[18]))
    # 保持登录状态
    def keep_login_cookie(self,url):
        return Cookie(self.driver).keep_login(url)
    # 添加已完成契约
    def add_finish_contract(self,companyName,contract_word,contract_appraise,url):
        self.keep_login_cookie(url)
        sleep(3)
        self.contract_list()
        sleep(3)
        self.add_contract_button()
        self.company_name(companyName)
        self.select_company()
        self.select_time()
        self.contract_describe(contract_word)
        self.select_finish_contracr(contract_appraise)
        self.add_contracr_verify()
    # 添加未完成契约,未选择防伪印章
    def add_unfinish_contract(self,url,companyName,contract_word):
        self.keep_login_cookie(url)
        sleep(2)
        self.contract_list()
        sleep(2)
        self.add_contract_button()
        sleep(2)
        self.company_name(companyName)
        self.select_company()
        self.select_time()
        self.contract_describe(contract_word)
        self.select_unfinish_contract()
        self.add_contracr_verify()
if __name__ == '__main__':
    con = Add_Contract(driver=webdriver.Firefox())
    companyName = '千帆渡'
    contract_word = '这是契约描述'
    contract_appraise = '这是契约评价'
    url = readconfig.url_admin
    con.add_finish_contract(companyName,contract_word,contract_appraise,url)