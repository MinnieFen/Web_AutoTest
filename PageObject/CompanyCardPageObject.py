# coding:utf-8
from Base.BasePage import BasePage
from time import sleep
from Base.GetLoginCookie import Cookie
from selenium.webdriver.common.by import By

com_card_list = (By.XPATH,'//*[@id="sidebar-nav"]/div/nav/ul/li[3]/a/span')    # 企业名片侧边栏
com_logo = (By.XPATH,'//*[@id="enterprises_id_creat_card_from"]/div[1]/div/div/button')     # 选择上传logo
contact_person = (By.XPATH,'//*[@id="enterprises_id_contact_name"]')             # 联系人输入框
contact_phone = (By.XPATH,'//*[@id="enterprises_id_contact_phone"]')             # 联系电话输入框
contact_address = (By.XPATH,'//*[@id="enterprises_id_contact_address"]')         # 联系地址输入框
website = (By.XPATH,'//*[@id="enterprises_id_url"]')                             # 官网输入框
introduction = (By.XPATH,'//*[@id="enterprises_id_introduction"]')               # 简介输入框
submit_btn = (By.XPATH,'//*[@id="enterprises_id_creat_submit"]')                 # 提交按钮

class Company_Card(BasePage):
    # 保持登录状态
    def keep_login_cookie(self, url):
        return Cookie(self.driver).keep_login(url)
    # 点击企业认证侧边栏
    def click_attestation_list(self,url):
        self.keep_login_cookie(url)
        sleep(3)
        self.click_btn(*com_card_list)
        sleep(3)
    # 选择企业logo
    def select_logo(self,path):
        self.select_file(path,*com_logo)
        sleep(3)
    # 输入联系人
    def send_person(self,name):
        self.clear_word(*contact_person)
        self.send_word(name,*contact_person)
        sleep(2)
    # 输入联系电话
    def send_phone(self,phone):
        self.clear_word(*contact_phone)
        self.send_word(phone,*contact_phone)
        sleep(2)
    # 输入联系地址
    def send_address(self,address):
        self.clear_word(*contact_address)
        self.send_word(address,*contact_address)
        sleep(2)
    # 输入官网
    def send_website(self,website_url):
        self.clear_word(*website)
        self.send_word(website_url,*website)
        sleep(2)
    # 输入简介
    def send_introduction(self,introduction_text):
        self.clear_word(*introduction)
        self.send_word(introduction_text,*introduction)
        sleep(2)
    # 点击提交按钮
    def click_submit(self):
        self.click_btn(*submit_btn)
        sleep(3)
    # 提交数据
    def submit_card(self,url,path,name,phone,address,website,introduction):
        self.click_attestation_list(url)
        self.select_logo(path)
        self.send_person(name)
        self.send_phone(phone)
        self.send_address(address)
        self.send_website(website)
        self.send_introduction(introduction)
        self.click_submit()
        sleep(3)

