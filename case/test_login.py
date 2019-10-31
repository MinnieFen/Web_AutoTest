# coding:utf-8
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.by import By
from config import readconfig
from common.operate_page import BasePage
from common import get_exceldata
class Login(unittest.TestCase):
    def setUp(self):
        self.d = webdriver.Chrome()
        url = readconfig.url
        self.d.get(url)
        self.B = BasePage(self.d)
        self.B.max_window()
        getdata = get_exceldata.get_excel_data('loginpage')
        self.data1 = getdata[0]['elements']
        self.data2 = getdata[1]['elements']
        self.data3 = getdata[2]['elements']
        self.data4 = getdata[3]['elements']
        self.data5 = getdata[4]['elements']
        self.data6 = getdata[5]['elements']
    def tearDown(self):
        pass
# 封装元素操作方法
    def test_login1(self):
        inputPhone = readconfig.inputPhone
        inputPsw = readconfig.inputPsw
        # B = BasePage(self.d)
        ele1 = (By.XPATH,self.data1)
        ele2 = (By.XPATH,self.data2)
        ele3 = (By.XPATH,self.data3)
        ele4 = (By.XPATH,self.data4)
        ele5 = (By.XPATH,self.data5)
        ele6 = (By.XPATH, self.data6)
        self.B.click_btn(*ele1)
        self.B.click_btn(*ele2)
        self.B.send_word(inputPhone,*ele3)
        self.B.send_word(inputPsw,*ele4)
        self.B.click_btn(*ele5)
        sleep(3)
        userName = self.B.get_text(*ele6)
        self.assertEqual(userName, u'晨曦')
        self.d.get_cookie(name = 'laravel_session')
        self.d.quit()

# 数据分离
#     def test_login1(self):
#         inputPhone = readconfig.inputPhone
#         inputPsw = readconfig.inputPsw
#         # B = BasePage(self.d)
#         ele1 = (By.XPATH,self.data1)
#         ele2 = (By.XPATH,self.data2)
#         ele3 = (By.XPATH,self.data3)
#         ele4 = (By.XPATH,self.data4)
#         ele5 = (By.XPATH,self.data5)
#         ele6 = (By.XPATH, self.data6)
#         self.B.find_web_element(*ele1).click()
#         self.B.find_web_element(*ele2).click()
#         self.B.find_web_element(*ele3).send_keys(inputPhone)
#         self.B.find_web_element(*ele4).send_keys(inputPsw)
#         self.B.find_web_element(*ele5).click()
#         sleep(3)
#         userName = self.B.find_web_element(*ele6).text
#         self.assertEqual(userName, u'晨曦')
#         self.d.quit()

    # def test_login1(self):
    #     inputPhone = readconfig.inputPhone
    #     inputPsw = readconfig.inputPsw
    #     B = BasePage(self.d)
    #     ele1 = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a')
    #     ele2 = (By.XPATH,'//*[@id="login_span_type_pwd"]')
    #     ele3 =(By.XPATH,'// *[@id = "login_id_input_phone"]')
    #     ele4 = (By.XPATH,'//*[@id ="login_id_input_password"]')
    #     ele5 = (By.XPATH,'//*[@id="login_id_login"]')
    #     B.find_web_element(*ele1).click()
    #     B.find_web_element(*ele2).click()
    #     B.find_web_element(*ele3).send_keys(inputPhone)
    #     B.find_web_element(*ele4).send_keys(inputPsw)
    #     B.find_web_element(*ele5).click()
    #     sleep(3)
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login('test_login1'))
    runner = unittest.TextTestRunner()
    runner.run(suite)