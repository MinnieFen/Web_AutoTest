# -*- codinfg:utf-8 -*-
'''
@author: Jeff LEE
@file: 翻页.py
@time: 2018-09-26 11:14
@desc:
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
# 添加智能等待
driver.implicitly_wait(10)

driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('uniquefu')

driver.find_element_by_id('su').click()

page = driver.find_element_by_id('page')
pages = page.find_elements_by_tag_name('a')  # 查找所有翻页跳转链接
time.sleep(5)

js = 'document.documentElement.scrollTop=10000'
total = 0  # 页面数
is_next_page = True  # 存在下一页
page_num = 0  # 要点击的页面号

# 往后翻页
while page_num < 10:  # 也可以通过is_next_page进行判断循环
    driver.execute_script(js)
    page_num = page_num + 1  # 设置页号为下一页
    total = page_num  # 记录页面数
    value = str(page_num)
    try:
        # 查找指定页面
        xpath = "//div[@id='page']/a[contains(@href,'pn=%s')]" % value
        print(xpath)
        one_page = driver.find_element_by_xpath(xpath)
        one_page.click()
        time.sleep(1)
        driver.execute_script(js)
        time.sleep(1)

    except:
        print('no next page')
        is_next_page = False
        total = total - 1
        break

    # 往前翻页
while total >= 0:

    driver.execute_script(js)

    try:
        total = total - 1
        value = str(total)
        xpath = "//div[@id='page']/a[contains(@href,'pn=%s')]" % value
        print(xpath)
        one_page = driver.find_element_by_xpath(xpath)
        one_page.click()
        time.sleep(1)
        driver.execute_script(js)
        time.sleep(1)

    except:
        print('no pre page')
        break

time.sleep(3)
driver.quit()