# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
class BasePage():
    def __init__(self,d):
        self.d = d
        # url = 'http://qiyuebao-t.yunxitech.cn/'
        # self.d.get(url)
    def find_web_element(self,*loc):
        return self.d.find_element(*loc)
# if __name__ == '__main__':
#     d = webdriver.Firefox()
#     test = BasePage(d)
#     test.find_element(By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a')