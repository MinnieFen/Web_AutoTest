# coding:utf-8
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.by import By
from config import readconfig
from common import get_exceldata
from common.operate_page import BasePage


class Login(unittest.TestCase):
    def setUp(self):
        self.d = webdriver.Chrome()
        url = readconfig.url_login
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
    def test_login1(self):
        inputPhone = readconfig.inputPhone_login
        inputPsw = readconfig.inputPsw_login
        # B = BasePage(self.d)
        self.B.click_btn(By.XPATH,self.data1)
        self.B.click_btn(By.XPATH,self.data2)
        self.B.send_word(inputPhone,By.XPATH,self.data3)
        self.B.send_word(inputPsw,By.XPATH,self.data4)
        self.B.click_btn(By.XPATH,self.data5)
        sleep(3)
        userName = self.B.get_text(By.XPATH, self.data6)
        self.assertEqual(userName, u'陈嘻嘻')
        self.d.get_cookie(name = 'laravel_session')
        self.d.quit()
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login('test_login1'))
    runner = unittest.TextTestRunner()
    runner.run(suite)