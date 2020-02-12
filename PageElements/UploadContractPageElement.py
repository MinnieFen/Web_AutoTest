# coding:utf-8
from selenium.webdriver.common.by import By
def contractProtect_elements():
    contract_protect_list = (By.XPATH,('/html/body/div[1]/div[1]/div/nav/ul/li[5]/a/span'))                     # 0 侧边栏 纸质合同数字保护
    select_contract_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div/div[3]/div[3]/div[2]/button'))       # 1 上传按钮
    toast_page = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div/div[3]/div[4]/div/div[2]/div[1]/p/span'))     # 2 弹框提示
    upload_error_server= (By.XPATH,'//*[@class = "layui-layer-content"]')                                       # 3 服务器提示
    upload_contract = (By.XPATH,'//*[@id="file"]')                                                              # 4 选择上传的文件
    contracted_btn = (By.XPATH,'//*[@class = "btn btn-primary look-protected-doc"]')                            # 5 查看已保护文档按钮
    search_word = (By.XPATH,'//*[@class = "cc-search-input"]')                                                  # 6 搜索文档框
    search_btn = (By.XPATH,'//*[@id = "cc-search-button"]')                                                     # 7 搜索按钮
    search_list = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[2]/div/div/div/div'))          # 8 获取搜索列表数据
    search_empty = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[2]/div/p'))                   # 9 搜索结果无数据
    return contract_protect_list,select_contract_btn,toast_page,upload_error_server,upload_contract,contracted_btn,search_word,search_btn,search_list,search_empty