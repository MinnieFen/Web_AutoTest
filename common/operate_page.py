# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
class BasePage():
    def __init__(self,d):
        self.d = d
# 定位元素
    def find_web_element(self,*loc):
        return self.d.find_element(*loc)
# 窗口最大化
    def max_window(self):
        return self.d.maximize_window()
# 元素点击操作
    def click_btn(self, *loc):
        return self.d.find_element(*loc).click()
# 元素输入内容
    def send_word(self, text,*loc,):
        return self.d.find_element(*loc).send_keys(text)
# 获取元素文本内容
    def get_text(self,*loc):
        return self.d.find_element(*loc).text
# 清空输入框
    def clear_word(self,*loc):
        return self.d.find_element(*loc).clear()
# 元素聚焦
    def ele_target(self,*loc):
        target = self.d.find_element(*loc)
        return self.d.excute_script("arguments[0].scrollIntoView();",target)


# if __name__ == '__main__':
#     url = 'http://qiyuebao-t.yunxitech.cn/'
#     d = webdriver.Firefox()
#     d.get(url)
#     B = BasePage(d)
#     ele = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a')
#     B.click_btn(*ele)
