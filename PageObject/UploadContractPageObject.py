# coding:utf-8
from PageElements.UploadContractPageElement import contractProtect_elements
from Base.BasePage import BasePage
from time import sleep
from Base.GetLoginCookie import Cookie

class Upload_contract(BasePage):
    # 进入选择文件页面
    def contract_protect_list(self,path):
        self.click_btn(*(contractProtect_elements()[0]))
        self.click_btn(*(contractProtect_elements()[1]))
        self.send_word(path,*(contractProtect_elements()[4]))
    # 进入查看已保护文档页面
    def contracted_page(self):
        self.click_btn(*(contractProtect_elements()[0]))
        sleep(2)
        self.click_btn(*(contractProtect_elements()[5]))
    # 前端提示信息
    def upload_page(self):
        return self.get_text(*(contractProtect_elements()[2]))
    # 服务器提示信息
    def upload_server(self):
        return self.get_text(*(contractProtect_elements()[3]))
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
        self.send_word(word,*(contractProtect_elements()[6]))
        sleep(2)
        self.click_btn(*(contractProtect_elements()[7]))
        sleep(3)
    # 获取搜索结果数据，断言与数据库查询结果做对比
    def search_result(self):
        list_result = self.find_web_elements(*(contractProtect_elements()[8]))
        lists = []
        for i in list_result:
            lists.append(i.text)    # 还要调试text获取到的内容，最好内获取文档名称
        # print(lists)
        return lists
    # 搜索结果无数据时，获取页面文本
    def search_empty_data(self):
        return self.get_text(*(contractProtect_elements()[9]))