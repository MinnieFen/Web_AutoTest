# coding:utf-8
from selenium import webdriver
from Base.BasePage import BasePage
from time import sleep
from PageElements.AddCompanyPageElements import addCompany_elements
from Base.SQLconnect import MySQLUtil
from Base.GetLoginCookie import Cookie
from config import readconfig
class Add_company(BasePage):
    # 点击展开公司列表
    def company_list(self):
        self.click_btn(*(addCompany_elements()[0]))
    # 点击添加公司按钮
    def add_company_button(self):
        self.click_btn(*(addCompany_elements()[1]))
    # 输入添加公司名称
    def add_companyName(self,companyName):
        self.send_word(companyName,*(addCompany_elements()[2]))
    # 确认添加公司
    def add_company_verify(self):
        self.click_btn(*(addCompany_elements()[3]))
    # hearde显示的公司名称
    def companyName(self):
        return self.get_text(*(addCompany_elements()[0]))
    # 添加公司，服务器报错信息
    def add_error_sever(self):
        return self.get_text(*(addCompany_elements()[5]))
    # 添加公司
    def add_company(self,phone,psw,urlcookie,companyName,url):
        cookie = Cookie()
        login_cookie = cookie.get_cookie(phone,psw,urlcookie)
        self.open_url(url)
        self.add_cookie(login_cookie)
        self.open_url(url)
        # cookie.keep_login(phone,psw,urlcookie,url)
        self.company_list()
        self.add_company_button()
        self.add_companyName(companyName)
        self.add_company_verify()
        sleep(5)
# if __name__ == '__main__':
#     a = Add_company(driver=webdriver.Firefox())
#     urlcookie = readconfig.url_login
#     phone = readconfig.inputPhone_cookie
#     psw = readconfig.inputPsw_cookie
#     url = readconfig.url_admin
#     companyName = '金控集团'
#     a.add_company(phone,psw,urlcookie,companyName,url)