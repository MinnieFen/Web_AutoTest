# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
d = webdriver.Firefox()
# d = webdriver.Chrome()

# 键盘操作事件
# d.get('https://baidu.com')
# d.find_element_by_id('kw').send_keys('selenium')
# d.find_element_by_id('su').submit()      # submit() 一般模拟回车键
# d.find_element_by_id('su').send_keys(Keys.ENTER)    # 操作键盘回车键

# 定位frame中的对象
# file_path = 'file:///'+os.path.abspath('frame.html')
# d.get(file_path)
# sleep(3)
# #frame 中有id或name属性时，直接用switch_to.frame方法去获取frame中嵌入的页面
# # d.switch_to.frame('f1')
# iframe = d.find_element_by_tag_name('iframe')    #frame中没有id或name属性时，先定位iframe
# d.switch_to.frame(iframe)
# d.switch_to.frame('f2')
# d.find_element_by_id('kw').send_keys('selenium')
# d.find_element_by_id('su').click()
# d.switch_to.default_content()   # 释放iframe，重新回到主页面上


# 多窗口处理
# d.get('https://www.baidu.com')
# d.find_element_by_link_text('登录').click()
# # 获取当前页面的句柄（handle）
# nowhandle = d.current_window_handle
# print(nowhandle)
# # sleep(3)
# d.implicitly_wait(10)
# # 打开注册页面新窗口
# d.find_element_by_class_name('tang-pass-footerBar').find_element_by_link_text('立即注册').click()   # 层级定位，先定位父级，再定位子级
# sleep(3)   # 若没有这句，则获取不到第二个页面的handle
# allhandles = d.window_handles   #获取所有窗口的handle
# print(allhandles)
# #方法一： 获取新句柄，判断句柄，不等于首页就切换
# # for handle in  allhandles:
# #     if handle != nowhandle:
# #         d.switch_to.window(handle)
# #         print(d.title)
# # 方法二：获取list里面的第二个直接切换
# d.switch_to.window(allhandles[1])
# print(d.title)    # 打印页面title
# d.close()   #关闭新窗口
# d.switch_to.window(nowhandle)    # 切换到首页句柄
# sleep(3)
# d.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()
# d.find_element_by_id('kw').send_keys('selenium')
# sleep(3)
# d.quit()

# alert/confirm/prompt 处理
# filepath = 'file:///'+ os.path.abspath('alerttest.html')
# d.get(filepath)
# sleep(3)
# d.find_element_by_id('alert').click()
# sleep(3)
# t1 = d.switch_to.alert    # 获取alert弹框
# print(t1.text)   # 打印警告内容
# t1.accept()      # 点击警告框确认按钮

# d.find_element_by_id('confirm').click()
# sleep(3)
# t2 = d.switch_to.alert
# print(t2.text)
# # t2.accept()      # 点击警告框确认按钮
# t2.dismiss()       # 点击警告框取消按钮

# d.find_element_by_id('prompt').click()
# sleep(3)
# t3 = d.switch_to.alert
# print(t3.text)
# t3.send_keys('hello selenium')
# t3.accept()
# d.quit()

# js处理滚动条
# d.get('https://www.cnblogs.com/yoyoketang/tag/selenium/')
# js = "window.scrollTo(0,1000)"       #控制右边滚动条，下拉 1000 的位置
# d.execute_script(js)
#
# js= "window.scrollTo(500,1000)"        # 横向和纵向移动滚动条
# d.execute_script(js)
# sleep(3)
#
# js = "window.scrollTo(0,0)"            # 横向、纵向移动滚动条到最左和顶部位置
# d.execute_script(js)
#
# ele = d.find_element_by_id('PostsList1_rpPosts_TitleUrl_19')
# d.execute_script("arguments[0].scrollIntoView();",ele)         # 元素聚焦
# sleep(2)
# ele.click()       # 聚焦后再去操作ele元素
# sleep(3)
# d.quit()

# 单选框和复选框
# file_path = 'file:///' + os.path.abspath('checkbox.html')
# d.get(file_path)
# d.find_element_by_id('boy').click()
# sleep(3)
# s = d.find_element_by_id('boy').is_selected()   # 判断元素是否为选中状态
# print(s)         # 选中返回True，未选中返回False
# d.find_element_by_id('girl').click()
# # 复选框，方法一：单个定位
# d.find_element_by_id('c1').click()
# d.find_element_by_id('c2').click()
# d.find_element_by_id('c3').click()
# # 复选框，方法二：定位一组元素
# # checkbox = d.find_elements_by_xpath('//*[@type = "checkbox"]')
# checkbox = d.find_elements_by_css_selector('input[type = "checkbox"]')   # 获取到一组元素
# for i in checkbox:    #  find_elements 不能直接点击，用for循环一个个点击
#     i.click()
# d.quit()

# 上传文件
# file_path = 'file://'+os.path.abspath('upload_file.html')
# d.get(file_path)
# d.find_element_by_name('file').send_keys(r'C:\Users\cmf\Desktop\test111.doc')
# sleep(5)
# d.quit()

# 获取百度输入联想词
# d.get('https://baidu.com')
# d.find_element_by_id('kw').send_keys('selenium')
# sleep(3)
# eles = d.find_elements_by_css_selector(".bdsug-overflow")
# print(eles)
# for i in eles:
#     print(i.get_attribute('data-key'))
# if len(eles)>1:
#     eles[1].click()
#     print(d.current_url)
# else:
#     print("未获取到匹配的词")

# cookie相关操作
# d.get('http://qiyuebao-t.yunxitech.cn/')
# d.find_element_by_xpath('//*[@id="muenCloumn"]/li[2]/a').click()
# d.find_element_by_xpath('//*[@id="login_span_type_pwd"]').click()
# d.find_element_by_xpath('// *[@id = "login_id_input_phone"]').send_keys('18782038146')
# d.find_element_by_xpath('//*[@id ="login_id_input_password"]').send_keys('a123456')
# d.find_element_by_xpath('//*[@id="login_id_login"]').click()
# print(d.get_cookies())    # 获取所有cookie
# print(d.get_cookie(name = 'laravel_session'))  # 获取指定name的cookie
# sleep(1)
# d.delete_cookie(name='laravel_session')    # 删除指定name的cookie
# d.delete_all_cookies()     # 删除所有cookie
# d.quit()
# d.refresh()   # 刷新页面

# 绕过验证码
# from Base import get_yamldata
# cookievalue = get_yamldata.get_cookie()
# print(cookievalue)
# C3 = cookievalue
# C3 = {'name': 'laravel_session', 'value': 'I8RgJzmkHpK1JRQxwkq56P3rhPRvOLu1Y3Mdm2P6'}
# d.get('http://qiyuebao-t.yunxitech.cn/admin?id=1&lg=0')
# d.add_cookie(C3)
# d.get('http://qiyuebao-t.yunxitech.cn/admin?id=1&lg=0')
# sleep(4)
# d.quit()
# 元素定位参数化
# d.get('https://baidu.com')
# d.find_element(By.ID,'kw').send_keys('selenium')