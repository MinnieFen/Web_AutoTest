# coding:utf-8
from selenium.webdriver.common.by import By
def addContract_elements():
    my_contract_list = (By.XPATH,('/html/body/div[1]/div[1]/div/nav/ul/li[4]/a/span'))   # 0 侧边栏 我的契约
    add_contract_btn = (By.XPATH,('//*[@class = "btn btn-primary"]'))                    # 1 我的契约按钮
    company_input_word = (By.XPATH,('//*[@id="company-input"]')) # 2 对方公司输入框
    search_btn = (By.XPATH,('//*[@class = "ui-button company-button"]'))                   # 3 搜索按钮
    select_company = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[1]/div[2]/ul/li[1]/a'))    # 4 选择第一个公司
    contract_time_word = (By.XPATH,('//*[@class = "datepicker time-input"]'))              # 5 契约月份输入框
    contract_time_btn = (By.XPATH,('/html/body/div[5]/div[2]/table/tbody/tr/td/span[12]'))  # 6 12月
    contract_describe_word = (By.XPATH,('//*[@class = "describe-text"]'))                  # 7 契约描述
    contract_finish_btn = (By.XPATH,('//*[@class = "ui-radio type-over-title"]'))          # 8 已完成契约
    contract_appraise_word = (By.XPATH,('//*[@class = "over-describe-text"]'))             # 9 契约评价
    attitude = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[1]/div[1]/div/img[1]'))   # 10 态度1星评价
    quality = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[1]/div[2]/div/img[2]'))    # 11 质量2星评价
    efficiency = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[2]/div[1]/div/img[3]')) # 12 效率3星评价
    credit = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[2]/div[2]/div/img[4]'))     # 13 守信4星评价
    specialty = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[3]/div[1]/div/img[5]'))  # 14 专业5星评价
    contract_unfinish_btn = (By.XPATH,('//*[@class = "ui-radio type-ing-title"]'))         # 15 未完成契约
    use_stamp_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[8]/div[2]/div[1]/div[1]/label[1]'))   # 16 我方使用防伪印章
    other_use_stamp_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[8]/div[2]/div[1]/div[2]/label[1]'))   # 17 对方使用防伪印章
    add_contract_verify_btn = (By.XPATH,('//*[@class = "over-btn btn btn-primary"]'))          # 18 确认添加契约
    add_error_server = (By.XPATH,('//*[@class = "layui-layer-content layui-layer-padding"]'))  # 19 服务器错误提示
    add_error_page = (By.XPATH,('//*[@class = "ui-tips-before"]'))                              # 20 前端页面错误提示
    add_toast = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/p[1]'))      # 21 弹框提示对方不是防伪印章用户
    add_toast_user = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/p'))    # 22 弹框提示我方不是防伪印章用户

    all_page = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/ul/li[1]/a'))  # 23 全部列表
    wait_confirm = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/ul/li[2]/a')) # 24 待我确认列表
    wait_complete= (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/ul/li[3]/a'))  # 25 待我完成列表
    wait_appraise = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/ul/li[4]/a')) # 26 待我评价列表
    wait_other_confirm = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/ul/li[5]/a')) # 27 待对方确认列表
    wait_confirm_num = (By.XPATH,('//*[@id="waitermyconfirm"]'))                                         # 28 待我确认数量
    wait_complete_num = (By.XPATH,('//*[@id="waitermycomplete"]'))                                        # 29 待我完成数量
    wait_appraise_num = (By.XPATH,('//*[@id="waitermyappraise"]'))                                        # 30 待我评价数量
    wait_other_confirm_num = (By.XPATH,('//*[@id="waiterotherconfirm"]'))                                 # 31 待对方确认数量
    search_word = (By.XPATH,('//*[@class = "form-control"]'))                                             # 32 关键字（对方公司）搜索输入框
    search_other_btn = (By.XPATH,('//*[@class = "btn btn-primary"]'))                                     # 33 搜索按钮
    confirm_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/button[1]'))    # 34第一条确认完成契约按钮
    confirm_cancel = (By.XPATH,('//*[@id="cancelbtn"]'))                                                                     # 35 取消确认完成契约
    confirm_ensure = (By.XPATH,('//*[@id="confimbtn"]'))                                                                     # 36 确定确认完成契约
    refuse_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/button[2]'))     # 37第一条拒绝按钮
    refuse_word = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/form/textarea'))                        # 38 拒绝内容
    refuse_cancel = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[3]/button[1]'))                          # 39 取消拒绝
    refuse_ensure = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[3]/button[2]'))                          # 40 确认拒绝
    complete_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/button'))         # 41第一条完成契约按钮
    complete_cancle_btn = (By.XPATH,('//*[@id="cancelbtn"]'))                                                                    # 42 取消完成契约
    confirm_complete = (By.XPATH,('//*[@id="confimbtn"]'))                                                                   # 43 确认完成契约
    appraise_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[2]/button'))      # 44 评价按钮
    appraise_word = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/textarea'))                      # 45 评价内容输入框
    appraise_attitude = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[1]/span[2]/img[1]')) # 46 态度一星
    appraise_quality = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[2]/span[2]/img[2]'))  # 47 质量两星
    appraise_efficiency = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[3]/span[2]/img[3]')) # 48 效率三星
    appraise_credit = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[4]/span[2]/img[4]'))     # 49 守信四星
    appraise_specialty = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[5]/span[2]/img[5]'))  # 50 专业五星
    appraise_cancle_btn = (By.XPATH,('//*[@class = "btn btn-default"]'))                                                       # 51 取消评价
    appraise_ensure_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[3]/button[2]'))                          # 52 确认评价
    wait_other_confirm_edit = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div[2]/button[1]')) # 53 待对方确认，编辑按钮
    edit_time = (By.XPATH,('/html/body/div[5]/div[2]/table/tbody/tr/td/span[6]'))                                                  # 54 重新选择契约月份为6月
    wait_other_confirm_delet = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div[2]/button[2]')) # 55 删除待对方确认契约按钮
    delet_cancel = (By.XPATH,('//*[@id="cancelbtn"]'))                                                                              # 56 取消删除
    delet_ensure = (By.XPATH,('//*[@id="confimbtn"]'))                                                                              # 57 确认删除
    # describe_text = (By.LINK_TEXT('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[5]/div[1]/p[2]'))                      # 58 获取待确认列表描述内容
    all_list_pages = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/nav/ul/li/a'))       # 52 获取分页总数
    all_list_last_page = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/nav/ul/li[1]/a/span'))    # 53 上一页按钮
    all_list_next_page = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/nav/ul/li[5]/a/span'))    # 54 下一页按钮
    all_list_page_num = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div'))              # 55 获取一页的总数

    return my_contract_list,add_contract_btn,company_input_word,search_btn,select_company,contract_time_word,contract_time_btn,contract_describe_word,contract_finish_btn,\
            contract_appraise_word,attitude,quality,efficiency,credit,specialty,contract_unfinish_btn,use_stamp_btn,other_use_stamp_btn,add_contract_verify_btn,add_error_server, \
            add_error_page,add_toast,add_toast_user,all_page,wait_confirm,wait_complete,wait_appraise,wait_other_confirm,wait_confirm_num,wait_complete_num,wait_appraise_num, \
           wait_other_confirm_num,search_word,search_other_btn,confirm_btn,confirm_cancel,confirm_ensure,refuse_btn,refuse_word,refuse_cancel,\
           refuse_ensure,complete_btn,complete_cancle_btn,confirm_complete, appraise_btn,appraise_word,appraise_attitude,appraise_quality,appraise_efficiency,appraise_credit,\
           appraise_specialty,appraise_cancle_btn,appraise_ensure_btn,wait_other_confirm_edit,edit_time,wait_other_confirm_delet,delet_cancel,delet_ensure,all_list_pages,\
           all_list_last_page,all_list_next_page,all_list_page_num