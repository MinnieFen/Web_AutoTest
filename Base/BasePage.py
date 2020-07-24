# coding:utf-8
from time import sleep
from selenium.webdriver.common.keys import Keys
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
# 打开url
    def open_url(self,url):
        return self.driver.get(url)
# 窗口最大化
    def max_window(self):
        self.driver.maximize_window()
# # 定位元素方法
#     def locate_element(self, locatetype, value):
#         if locatetype == 'id':
#             el = self.driver.find_element_by_id(value)
#         if locatetype == 'name':
#             el = self.driver.find_element_by_name(value)
#         if locatetype == 'class_name':
#             el = self.driver.find_element_by_class_name(value)
#         if locatetype == 'tag_name':
#             el = self.driver.find_element_by_tag_name(value)
#         if locatetype == 'link':
#             el = self.driver.find_element_by_tag_name(value)
#         if locatetype == 'partial_link':
#             el = self.driver.find_element_by_partial_link_text(value)
#         if locatetype == 'css':
#             el = self.driver.find_element_by_css_selector(value)
#         if locatetype == 'xpath':
#             el = self.driver.find_element_by_xpath(value)
#         return el if el else None
# #点击元素
#     def click_btn(self,locatetype,value):
#         return self.locate_element(locatetype,value).click()
# 定位元素
    def find_web_element(self, *loc):
        return self.driver.find_element(*loc)
# 定位一组元素
    def find_web_elements(self,*loc):
        return self.driver.find_elements(*loc)
# 元素点击操作
    def click_btn(self, *loc):
        return self.driver.find_element(*loc).click()
# 元素输入内容
    def send_word(self, text,*loc,):
        return self.driver.find_element(*loc).send_keys(text)
# 获取元素文本内容
    def get_text(self,*loc):
        return self.driver.find_element(*loc).text
# 清空输入框
    def clear_word(self,*loc):
        return self.driver.find_element(*loc).clear()
# 元素聚焦
    def ele_target(self):
        # target = self.driver.find_element(*loc)
        # self.driver.execute_script("arguments[0].scrollIntoView();",target)
        js = 'var q = document.documentElement.scrollTop=10000'
        self.driver.execute_script(js)

# 获取登录cookie
    def get_login_cookie(self):
        return self.driver.get_cookie(name = 'laravel_session')
# 添加cookie
    def add_cookie(self,cookie):
        return self.driver.add_cookie(cookie)
# 刷新页面
    def refresh_window(self):
        self.driver.refresh()
        sleep(2)
# 上传文件
    def select_file(self,files,*loc):
        return self.driver.find_element(*loc).send_keys(files)     # 对input进行send_keys（） 不需要再去操作点击上传按钮，会导致多余的选择文件弹框出现
#获取当前的浏览器窗口
    def get_handle(self):
        return self.driver.current_window_handle
# if __name__ == '__main__':
#     url = 'http://qiyuebao-t.yunxitech.cn/'
#     d = webdriver.Firefox()
#     d.get(url)
#     B = BasePage(d)
#     ele = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a')
#     B.click_btn(*ele)
