# coding:utf-8
from Base.BasePage import BasePage
from time import sleep
from Base.GetLoginCookie import Cookie
from selenium.webdriver.common.by import By

contract_protect_list = (By.XPATH, ('/html/body/div[1]/div[1]/div/nav/ul/li[5]/a/span'))  # 0 侧边栏 纸质合同数字保护
select_contract_btn = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div/div[3]/div[3]/div[2]/button'))  # 1 上传按钮
toast_page = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div/div[3]/div[4]/div/div[2]/div[1]/p/span'))  # 2 弹框提示
upload_error_server = (By.XPATH, '//*[@class = "layui-layer-content"]')  # 3 服务器提示
upload_contract = (By.XPATH, '//*[@id="file"]')  # 4 选择上传的文件
contracted_btn = (By.XPATH, '//*[@class = "btn btn-primary look-protected-doc"]')  # 5 查看已保护文档按钮
search_word = (By.XPATH, '//*[@class = "cc-search-input"]')  # 6 搜索文档框
search_btn = (By.XPATH, '//*[@id = "cc-search-button"]')  # 7 搜索按钮
search_list = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[2]/div/div/div/div'))  # 8 获取搜索列表数据
search_empty = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[2]/div/p'))  # 9 搜索结果无数据
upload_toast = (By.XPATH,( '//*[@id="wrapper"]/div[2]/div/div/div/div[3]/div[4]/div/div[2]/div[1]/p/span'))      # 上传文件后，弹框提示信息
download_btn = (By.XPATH,'//*[@id="word-delete-ing-0"]/div[2]/div/a')    # 下载第一个文档
message_btn = (By.XPATH,'//*[@id="chark-certificate-button"]')       #  查看保全信息按钮
class Upload_contract(BasePage):
    # 进入选择文件页面
    def contract_protect_list(self,path):
        self.click_btn(*contract_protect_list)
        # self.click_btn(*select_contract_btn)     # 使用send_keys上传文件的方法，不需要再去操作点击上传，否则上传文件弹框会多显示一个
        self.select_file(path,*upload_contract)
    # 进入查看已保护文档页面
    def contracted_page(self):
        self.click_btn(*contract_protect_list)
        sleep(2)
        self.click_btn(*contracted_btn)
    # 保持登录状态
    def keep_login_cookie(self,url):
        return Cookie(self.driver).keep_login(url)
    # 上传合同
    def upload_contract(self,url,path):
        self.keep_login_cookie(url)
        sleep(3)
        self.contract_protect_list(path)
        sleep(3)
    # 搜索框输入内容
    def search(self,url,word):
        self.keep_login_cookie(url)
        sleep(2)
        self.contracted_page()
        self.send_word(word,*search_word)
        sleep(2)
        self.click_btn(*search_btn)
        sleep(3)
    # 获取搜索结果数据，断言与数据库查询结果做对比
    def search_result(self):
        list_result = self.find_web_elements(*search_list)
        lists = []
        for i in list_result:
            lists.append(i.text)    # 还要调试text获取到的内容，最好内获取文档名称
        # print(lists)
        return lists
    # 搜索结果无数据时，获取页面文本
    def search_empty_data(self):
        return self.get_text(*search_empty)
    # 上传文件后，弹框提示信息
    def upload_page_toast(self):
        return self.get_text(*upload_toast)
    # 下载文档
    def download_file(self,url):
        self.keep_login_cookie(url)
        sleep(3)
        self.click_btn(*download_btn)
        sleep(3)
    # 查看保全信息
    def protect_message(self,url):
        self.keep_login_cookie(url)
        sleep(3)
        self.click_btn(*message_btn)
        sleep(3)