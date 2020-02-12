# coding:utf-8
from Base.BasePage import BasePage
from time import sleep
from PageElements.AddContractPageElement import addContract_elements
from Base.GetLoginCookie import Cookie
from selenium import webdriver
from config import readconfig

class Add_Contract(BasePage):
    # 点击侧边栏我的契约
    def contract_list(self):
        self.click_btn(*(addContract_elements()[0]))
        sleep(3)
    # 点击添加契约按钮
    def add_contract_btn(self):
        self.click_btn(*(addContract_elements()[1]))
        sleep(3)
    # 输入公司名称，搜索
    def company_name(self,companyName):
        self.send_word(companyName,*(addContract_elements()[2]))
        self.click_btn(*(addContract_elements()[3]))
        sleep(3)
        self.click_btn(*(addContract_elements()[4]))       # 选择第一个公司
        self.click_btn(*(addContract_elements()[5]))       # 选择12月
        sleep(2)
        self.click_btn(*(addContract_elements()[6]))
        sleep(2)
    # 输入契约描述
    def contract_describe(self,contract_word):
        self.send_word(contract_word,*(addContract_elements()[7]))
    # 选择已完成契约，选择评价等级
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
    # 服务器错误提示
    def add_error_sever(self):
        return self.get_text(*(addContract_elements()[19]))
    # 前端错误提示
    def add_error_page(self):
        return self.get_text(*(addContract_elements()[20]))
    # 弹框提示对方不是印章用户
    def add_toast(self):
        return self.get_text(*(addContract_elements()[21]))
    # 弹框提示我方不是印章用户
    def add_toast_user(self):
        return self.get_text(*(addContract_elements()[22]))
    # 前端错误提示
    def contract_error_page(self):
        return self.get_text(*(addContract_elements()[19]))
    # 添加已完成契约
    def add_finish_contract(self,url,companyName,contract_word,contract_appraise):
        self.keep_login_cookie(url)
        sleep(3)
        self.contract_list()
        self.add_contract_btn()
        self.company_name(companyName)
        self.contract_describe(contract_word)
        self.select_finish_contracr(contract_appraise)
        self.add_contracr_verify()
        sleep(2)
    # 添加未完成契约,未选择防伪印章
    def add_unfinish_contract(self,url,companyName,contract_word):
        self.keep_login_cookie(url)
        sleep(2)
        self.contract_list()
        self.add_contract_btn()
        self.company_name(companyName)
        self.contract_describe(contract_word)
        self.select_unfinish_contract()
        self.add_contracr_verify()
        sleep(3)
    # 添加未完成契约，选择我方使用防伪印章
    def add_unfinish_use_stamp(self,url,companyName,contract_word):
        self.keep_login_cookie(url)
        sleep(2)
        self.contract_list()
        self.add_contract_btn()
        self.company_name(companyName)
        self.contract_describe(contract_word)
        self.select_unfinish_contract()
        self.select_use_stamp()
        self.add_contracr_verify()
        sleep(3)
    # 添加未完成契约，选择对方使用防伪印章
    def add_unfinish_other_use_stamp(self,url,companyName,contract_word):
        self.keep_login_cookie(url)
        sleep(2)
        self.contract_list()
        self.add_contract_btn()
        self.company_name(companyName)
        self.contract_describe(contract_word)
        self.select_unfinish_contract()
        self.select_other_use_stamp()
        self.add_contracr_verify()
        sleep(3)
    # 添加未完成契约，双方都使用防伪印章
    def add_unfinish_all_use_stamp(self,url,companyName,contract_word):
        self.keep_login_cookie(url)
        sleep(2)
        self.contract_list()
        self.add_contract_btn()
        self.company_name(companyName)
        self.contract_describe(contract_word)
        self.select_unfinish_contract()
        self.select_use_stamp()
        self.select_other_use_stamp()
        self.add_contracr_verify()
        sleep(3)
    # 选择待我确认列表
    def select_wait_confirm(self,url):
        self.keep_login_cookie(url)
        sleep(3)
        self.contract_list()
        sleep(2)
        self.click_btn(*(addContract_elements()[24]))
    # 待我确认数量
    def wait_confirm_num(self):
        return self.get_text(*(addContract_elements()[28]))
    # 确认完成契约
    def confirm_ensure(self,url):
        self.select_wait_confirm(url)
        self.click_btn(*(addContract_elements()[34]))
        self.click_btn(*(addContract_elements()[36]))
    # 取消确认完成契约
    def confirm_cancel(self,url):
        self.select_wait_confirm(url)
        self.click_btn(*(addContract_elements()[34]))
        self.click_btn(*(addContract_elements()[35]))
    # 选择拒绝契约
    def select_refuse(self,url):
        self.select_wait_confirm(url)
        self.click_btn(*(addContract_elements()[37]))
    # 确认拒绝契约
    def refuse_ensure(self,url,reason):
        self.select_refuse(url)
        self.send_word(reason,*(addContract_elements()[38]))
        sleep(3)
        self.click_btn(*(addContract_elements()[40]))
    # 取消拒绝契约
    def refuse_cancel(self,url,reason):
        self.select_refuse(url)
        self.send_word(reason,*(addContract_elements()[38]))
        self.click_btn(*(addContract_elements()[39]))
    # 选择待我完成契约列表
    def select_wait_complete(self,url):
        self.keep_login_cookie(url)
        sleep(3)
        self.click_btn(*(addContract_elements()[25]))
    # 待我完成列表数量
    def wait_complete_num(self):
        return self.get_text(*(addContract_elements()[29]))
    # 确认完成契约
    def complete_ensure(self,url):
        self.select_wait_complete(url)
        self.click_btn(*(addContract_elements()[41]))
        self.click_btn(*(addContract_elements()[43]))
    # 取消完成契约
    def complete_cancel(self,url):
        self.select_wait_complete(url)
        self.click_btn(*(addContract_elements()[41]))
        self.click_btn(*(addContract_elements()[42]))
    # 选择待我评价列表
    def select_wait_appraise(self,url):
        self.keep_login_cookie(url)
        sleep(3)
        self.click_btn(*(addContract_elements()[26]))
        self.click_btn(*(addContract_elements()[44]))
    # 待我评价列表数量
    def wait_appraise_num(self):
        return self.get_text(*(addContract_elements()[30]))
    # 输入评价内容
    def appraise_content(self,url,content):
        self.select_wait_appraise(url)
        self.send_word(content,*(addContract_elements()[45]))
    # 选择评价星级
    def appraise_grade(self):
        self.click_btn(*(addContract_elements()[46]))
        self.click_btn(*(addContract_elements()[47]))
        self.click_btn(*(addContract_elements()[48]))
        self.click_btn(*(addContract_elements()[49]))
        self.click_btn(*(addContract_elements()[50]))
    # 确认评价，选择评价等级
    def appraise_ensure(self,url,content):
        self.appraise_content(url,content)
        self.appraise_grade()
        self.click_btn(*(addContract_elements()[52]))
    # 确认评价，不选择评价等级
    def appraise_empty_grade(self,url,content):
        self.appraise_content(url,content)
        self.click_btn(*(addContract_elements()[52]))
    # 取消评价，选择评价等级
    def appraise_cancel(self,url,content):
        self.appraise_content(url,content)
        self.appraise_grade()
        self.click_btn(*(addContract_elements()[51]))
    # 取消评价,不选择评价等级
    def appraise_cancel_empty(self,url,content):
        self.appraise_content(url,content)
        self.click_btn(*(addContract_elements()[51]))
    # 待对方确认列表
    def select_wait_other_confirm(self,url):
        self.keep_login_cookie(url)
        sleep(3)
        self.click_btn(*(addContract_elements()[27]))
    # 待对方确认数量
    def wait_other_confirm_num(self):
        return self.get_text(*(addContract_elements()[31]))
    # 编辑契约，不修改直接确认
    def unaltered_ensure(self,url):
        self.select_wait_other_confirm(url)
        self.click_btn(*(addContract_elements()[53]))
        self.click_btn(*(addContract_elements()[18]))
    # 编辑契约，重新选择月份，重新输入描述
    def alter_time_ensure(self,url,decrible):
        self.select_wait_other_confirm(url)
        self.click_btn(*(addContract_elements()[53]))
        self.click_btn(*(addContract_elements()[54]))
        self.send_word(decrible,*(addContract_elements()[7]))
        self.click_btn(*(addContract_elements()[18]))

# if __name__ == '__main__':
    # con = Add_Contract(driver=webdriver.Firefox())
#     companyName = '千帆渡'
#     contract_word = '这是契约描述'
#     contract_appraise = '这是契约评价'
#     url = readconfig.url_admin
#     con.add_finish_contract(companyName,contract_word,contract_appraise,url)
#     con.confirm_ensure(url)