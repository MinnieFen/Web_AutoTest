# conding:utf-8
from selenium.webdriver.common.by import By
def addCompany_elements():
    company_list_btn = (By.XPATH,'//*[@class = "company-name"]')    # 点击展开公司列表
    add_company_btn = (By.XPATH,'//*[@class = "lnr lnr-plus-circle"]')     # 点击添加公司按钮
    company_name_word = (By.XPATH,'//*[@class = "form-control"]')        # 公司名称输入框
    verify_add_company_btn = (By.XPATH,'//*[@class = "btn btn-primary"]')    # 确认添加公司
    company_name_text = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a')    # header显示公司名称
    add_error_sever = (By.XPATH,'//*[@class = "layui-layer-content layui-layer-padding"]')      # 服务器错误信息提示
    return company_list_btn,add_company_btn,company_name_word,verify_add_company_btn,company_name_text,add_error_sever
# addCompany_elements()