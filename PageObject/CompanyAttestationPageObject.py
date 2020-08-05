# coding:utf-8
from Base.BasePage import BasePage
from time import sleep
from Base.GetLoginCookie import Cookie
from selenium.webdriver.common.by import By

com_attestation_list = (By.XPATH,'/html/body/div[1]/div[1]/div/nav/ul/li[2]/a/span')  # 企业认证侧边栏
com_code_text = (By.XPATH,'//*[@id="company-code"]')    # 企业代码输入框
com_email_text = (By.XPATH,'//*[@id="company-email"]')    # 邮箱输入框
com_lecense_image = (By.XPATH,'//*[@id="company-yyzz"]')    # 上传营业执照按钮
submit_btn = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/p[2]/button')    # 提交审核按钮
code_toast = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[2]/div[2]/p/span')   # 请输入正确的企业代码
email_toast = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[3]/div[2]/p/span')  # 请输入正确的企业邮箱
lisence_toast = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[4]/div[2]/p/span')  # 请选择您要上传的图片
check_btn = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[4]/div/div[1]/div[2]/p')        # 审核中文字
class Com_Attestation(BasePage):
    # 保持登录状态
    def keep_login_cookie(self, url):
        return Cookie(self.driver).keep_login(url)
    # 点击企业认证侧边栏
    def click_attestation_list(self,url):
        self.keep_login_cookie(url)
        sleep(3)
        self.click_btn(*com_attestation_list)
        sleep(3)
    # 输入企业代码和邮箱
    def send_text(self,code,email):
        self.clear_word(*com_code_text)
        self.send_word(code,*com_code_text)
        self.clear_word(*com_email_text)
        self.send_word(email,*com_email_text)
        sleep(3)
    # 选择营业执照上传
    def select_image(self,path):
        self.select_file(path,*com_lecense_image)
        sleep(3)
    # 提交认证审核
    def submit_attestation(self,url,code,email,path):
        self.click_attestation_list(url)
        self.send_text(code,email)
        self.select_image(path)
        self.click_btn(*submit_btn)
        sleep(3)
    # 企业代码错误提示信息
    def com_code_toast(self):
        self.get_text(*code_toast)
    # 企业邮箱错误提示信息
    def com_email_toast(self):
        self.get_text(*email_toast)
    # 营业执照错误提示信息
    def com_lisence_toast(self):
        self.get_text(*lisence_toast)
    # 提交审核成功后，审核中标签显示
    def check_text(self):
        self.get_text(*check_btn)