# conding:utf-8
from selenium.webdriver.common.by import By
def addCompany_elements():
    card_list = (By.XPATH,('/html/body/div[1]/div[1]/div/nav/ul/li[3]/a/span'))
    company_logo = (By.XPATH,('//*[@class = "enterprises-not-creat-select-logo-tip"]'))

    return card_list,company_logo