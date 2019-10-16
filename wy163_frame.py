# coding:utf-8
from selenium import webdriver
import os
from time import sleep
d = webdriver.Firefox()
# d.get('https://qiye.163.com/login/')
# d.find_element_by_id('switchNormalCtrl').click()
# d.find_element_by_id('accname').send_keys('chenmingfen@yunxitech.cn')
# d.find_element_by_id('accpwd').send_keys('cmf437889925')
# sleep(3)
# d.find_element_by_xpath('/html/body/section/div/div[2]/div[2]/form[1]/div[5]/button').click()

file_path = 'file:///'+os.path.abspath('frame.html')
d.get(file_path)
sleep(3)
d.switch_to.frame('f1')
d.switch_to.frame('f2')
d.find_element_by_id('kw').send_keys('selenium')
d.find_element_by_id('su').click()
sleep(3)
d.quit()
