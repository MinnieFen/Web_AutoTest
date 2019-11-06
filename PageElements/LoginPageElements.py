# coding:utf-8
from selenium.webdriver.common.by import By
from selenium import webdriver
# class Loginpage_elements():
#     def __init__(self):
#         pass
#     def login_elements(self):
#         self.login_page_btn = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a')     # 跳转登录页面
#         self.psw_login_btn =(By.XPATH, '//*[@id="login_span_type_pwd"]')    # 切换密码登录
#         self.phone_word = (By.XPATH,'// *[@id = "login_id_input_phone"]')   # 输入手机号
#         self.psw_word = (By.XPATH,'//*[@id ="login_id_input_password"]')    # 输入密码/验证码
#         self.login_btn = (By.XPATH,'//*[@id="login_id_login"]')     # 确定登录
#         self.user_name = (By.XPATH,'//*[@class = "dropdown-toggle"]')   # 登录成功header显示的用户名
#         self.get_code_btn = (By.XPATH,'//*[@id = "login_button_get_sms_code"]')     # 点击获取验证码
#         self.forgot_psw_btn = (By.XPATH,'/html/body/div[1]/div/div/form/div[1]/div[5]/a')   # 点击忘记密码
#         self.new_psw_word = (By.XPATH,'//*[@id = "login_id_input_password_new"]')   # 输入新密码
#         self.register_page_btn = (By.XPATH,'/html/body/div[1]/div/div/form/div[2]/a')   # 点击立即注册
#         self.register_phone_word = (By.XPATH,'//*[@id = "user-phone-input"]')   # 输入注册手机号
#         self.register_psw_word = (By.XPATH,'//*[@id = "password-input"]')   # 输入注册密码
#         self.register_name_word = (By.XPATH,'//*[@id = "user-name-input"]')     # 输入注册用户名
#         self.register_code_btn = (By.XPATH,'//*[@id = "v-code-btn"]')       # 点击注册获取验证码
#         self.register_code_word = (By.XPATH,'//*[@id = "v-code-input"]')    # 输入注册验证码
#         self.agree_deal_btn = (By.XPATH,'//*[@class = "ui-checkbox wyydfwxy"]')     # 勾选同意服务协议框
#         self.confirm_register_btn = (By.XPATH,'//*[@id = "register-button"]')       # 确定注册按钮
#         self.back_to_homepage = (By.XPATH,'/html/body/nav/div/div[1]/a/span/span[1]')       # 返回首页
#         self.logout_btn = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/ul/li[4]/a')        # 点击退出按钮
#         return (self.login_page_btn,self.psw_login_btn,self.phone_word,self.psw_word,self.login_btn,self.user_name,self.get_code_btn,self.forgot_psw_btn,self.new_psw_word,
#         self.register_page_btn,self.register_phone_word,self.register_psw_word,self.register_name_word,self.register_code_btn,self.register_code_word,self.agree_deal_btn,
#         self.confirm_register_btn,self.back_to_homepage,self.logout_btn)
def login_elements():
    d = webdriver.Firefox()
    login_page_btn = ('/html/body/nav/div/div[2]/ul/li[2]/a')     # 跳转登录页面
    psw_login_btn =(By.XPATH, '//*[@id="login_span_type_pwd"]')    # 切换密码登录
    phone_word = (By.XPATH,'// *[@id = "login_id_input_phone"]')   # 输入手机号
    psw_word = (By.XPATH,'//*[@id ="login_id_input_password"]')    # 输入密码/验证码
    login_btn = (By.XPATH,'//*[@id="login_id_login"]')     # 确定登录
    user_name = (By.XPATH,'//*[@class = "dropdown-toggle"]')   # 登录成功header显示的用户名
    get_code_btn = (By.XPATH,'//*[@id = "login_button_get_sms_code"]')     # 点击获取验证码
    forgot_psw_btn = (By.XPATH,'/html/body/div[1]/div/div/form/div[1]/div[5]/a')   # 点击忘记密码
    new_psw_word = (By.XPATH,'//*[@id = "login_id_input_password_new"]')   # 输入新密码
    register_page_btn = (By.XPATH,'/html/body/div[1]/div/div/form/div[2]/a')   # 点击立即注册
    register_phone_word = (By.XPATH,'//*[@id = "user-phone-input"]')   # 输入注册手机号
    register_psw_word = (By.XPATH,'//*[@id = "password-input"]')   # 输入注册密码
    register_name_word = (By.XPATH,'//*[@id = "user-name-input"]')     # 输入注册用户名
    register_code_btn = (By.XPATH,'//*[@id = "v-code-btn"]')       # 点击注册获取验证码
    register_code_word = (By.XPATH,'//*[@id = "v-code-input"]')    # 输入注册验证码
    agree_deal_btn = (By.XPATH,'//*[@class = "ui-checkbox wyydfwxy"]')     # 勾选同意服务协议框
    confirm_register_btn = (By.XPATH,'//*[@id = "register-button"]')       # 确定注册按钮
    back_to_homepage = (By.XPATH,'/html/body/nav/div/div[1]/a/span/span[1]')       # 返回首页
    logout_btn = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/ul/li[4]/a')        # 点击退出按钮
    return (login_page_btn, psw_login_btn, phone_word, psw_word, login_btn, user_name,get_code_btn, forgot_psw_btn, new_psw_word,
            register_page_btn,register_phone_word,register_psw_word,register_name_word,register_code_btn,register_code_word,agree_deal_btn,
            confirm_register_btn,back_to_homepage,logout_btn)
login_elements()
print(login_elements())